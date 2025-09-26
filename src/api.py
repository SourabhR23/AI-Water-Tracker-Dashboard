from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history, get_today_total_intake
from src.logger import log_message

# Initialize FastAPI app and Agent
app = FastAPI()
agent = WaterIntakeAgent()

# Define variables type for Base Model
class WaterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

# Endpoint to log water intake
@app.post("/log-intake/")
async def log_water_intake(request: WaterIntakeRequest):
    """ Log user's water intake and get hydration analysis. """
    log_intake(request.user_id, request.intake_ml)
    total_intake = get_today_total_intake(request.user_id)
    analysis = agent.analyze_intake(total_intake)
    log_message(f"User {request.user_id} logged {request.intake_ml} ml")
    return {"message": "Water intake logged successfully", "analysis": analysis}

# Endpoint to get water intake history
@app.get("/history/{user_id}")
async def get_water_history(user_id: str):
    """ Retrieve the user's water intake history. """
    history = get_intake_history(user_id)
    return {"user_id": user_id, "history": history}
