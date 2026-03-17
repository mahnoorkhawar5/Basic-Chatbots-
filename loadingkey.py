from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file
api_key = os.getenv("MISTRAL_API_KEY")

print(api_key)  # just to verify, it should print your key