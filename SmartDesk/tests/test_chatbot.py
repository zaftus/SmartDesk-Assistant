import pytest
from smartdesk.chatbot import Chatbot

def test_chatbot_greeting():
    bot = Chatbot()
    response = bot.get_response("hello")
    assert response in ["Hello!", "Hi there!", "Hey! How can I help?"]
