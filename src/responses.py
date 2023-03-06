from revChatGPT.V1 import AsyncChatbot
from revChatGPT.V3 import Chatbot
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_EMAIL = os.getenv("OPENAI_EMAIL")
OPENAI_PASSWORD = os.getenv("OPENAI_PASSWORD")
SESSION_TOKEN = os.getenv("SESSION_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ENGINE = os.getenv("OPENAI_ENGINE")
CHAT_MODEL = os.getenv("CHAT_MODEL")

if CHAT_MODEL ==  "UNOFFICIAL":
    unofficial_chatbot = AsyncChatbot(config={"email":OPENAI_EMAIL, "password":OPENAI_PASSWORD, "session_token":SESSION_TOKEN})
elif CHAT_MODEL == "OFFICIAL":
    offical_chatbot = Chatbot(api_key=OPENAI_API_KEY, engine=ENGINE)

async def official_handle_response(message) -> str:
    return offical_chatbot.ask(message)

async def unofficial_handle_response(message) -> str:
    async for response in unofficial_chatbot.ask(message):
        responseMessage = response["message"]

    return responseMessage