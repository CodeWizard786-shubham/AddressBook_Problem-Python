import logging

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
        logging.StreamHandler(),  # Stream logs to the console
        logging.FileHandler('address_book_system.log')  # Store logs in a file
    ])

# creating a logger
logger = logging.getLogger(__name__)



