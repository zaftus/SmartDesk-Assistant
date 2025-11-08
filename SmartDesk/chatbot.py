import json
import random
from .config import DATA_DIR

class Chatbot:
    def __init__(self):
        self.intents = self.load_intents()

    def load_intents(self):
        with open(f"{DATA_DIR}/intents.json", "r") as f:
            return json.load(f)

    def get_response(self, user_input):
        for intent in self.intents["intents"]:
            if any(word in user_input.lower() for word in intent["patterns"]):
                return random.choice(intent["responses"])
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    bot = Chatbot()
    while True:
        inp = input("You: ")
        print("Bot:", bot.get_response(inp))
