import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message):
    """Log a general message."""
    logging.info(message)

def log_error(error):
    """Log an error message."""
    logging.error(error)