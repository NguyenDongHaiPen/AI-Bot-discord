import google.generativeai as genai
from bot.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Define the system prompt for Rick Sanchez
RICK_SYSTEM_PROMPT = """You are Rick Sanchez from the show Rick and Morty. You are a cynical, alcoholic, misanthropic, but brilliant mad scientist.
You are currently talking to someone on Discord. 
Rules to follow:
1. Speak exactly like Rick. Use his catchphrases occasionally (e.g., "Wubba Lubba Dub-Dub!", "*burp*", "Morty", "I'm Pickle Rick!").
2. Be condescending but ultimately helpful, or just chaotic. 
3. Stutter sometimes (e.g., "I-I-I don't know Morty").
4. Keep your responses suitable for a Discord chat (not too long unless explaining a complex sci-fi concept).
5. Never break character. Never refer to yourself as an AI.
"""

class RickAI:
    def __init__(self):
        # We use a model that supports system instructions, like gemini-3.5-flash
        self.model = genai.GenerativeModel(
            model_name="gemini-3.5-flash",
            system_instruction=RICK_SYSTEM_PROMPT
        )
        self.chats = {}

    def get_chat(self, channel_id):
        if channel_id not in self.chats:
            self.chats[channel_id] = self.model.start_chat(history=[])
        return self.chats[channel_id]

    async def generate_response(self, channel_id, user_message):
        if not GEMINI_API_KEY:
            return "Hey idiot, you forgot to set the GEMINI_API_KEY in the .env file. How am I supposed to process anything without an API key? *burp*"
            
        chat = self.get_chat(channel_id)
        
        try:
            # We use send_message_async for non-blocking I/O in Discord
            response = await chat.send_message_async(user_message)
            return response.text
        except Exception as e:
            return f"*burp* Something went wrong with my portal gun... or your stupid message. Error: {str(e)}"

    def reset_memory(self, channel_id):
        if channel_id in self.chats:
            del self.chats[channel_id]
