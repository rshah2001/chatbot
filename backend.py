import openai
import os
from dotenv import load_dotenv

load_dotenv('.env.local')
class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant'},
                {'role': 'user', 'content': user_input}
            ],
            max_tokens=2000,
            temperature=0.5
        )

        return response.choices[0].message['content']


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about Planes")
    print(response)
