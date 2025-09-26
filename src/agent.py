import requests
from dotenv import load_dotenv
import os

load_dotenv()
EURI_API_KEY = os.getenv("EURI_API_KEY")

class WaterIntakeAgent:
    """AI agent to track and suggest daily water intake."""

    def __init__(self):
        self.history = []
    
    def analyze_intake(self, recent_intake_ml, total_intake_ml):
        url = "https://api.euron.one/api/v1/euri/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {EURI_API_KEY}"  # Make sure to keep this secure
        }
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": f"You are a hydration assistant. The user has consumed recently i.e now {recent_intake_ml} and today total consumed is {total_intake_ml} ml of water today. Provide a hydration status and suggest if they need to drink more water."
                }
            ],
            "model": "gpt-4.1-nano",
            "max_tokens": 1000,
            "temperature": 0.7
        }
        
        # Make the POST request to the EURI API
        response = requests.post(url, headers=headers, json=payload)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            # Access the returned content
            return data['choices'][0]['message']['content']  # Ensure the structure is correct
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "An error occurred while fetching the response."

# Example usage
if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 750
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Analysis: {feedback}")