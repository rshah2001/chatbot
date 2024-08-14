
<img width="694" alt="Screenshot 2024-08-14 at 1 22 23 PM" src="https://github.com/user-attachments/assets/218dca13-4868-4542-be95-6779d86676fa">

# Chatbot GUI Application

This is a simple Chatbot GUI application built using PyQt6 and OpenAI's GPT-3.5 API. Users can input their queries, and the chatbot will respond using the OpenAI API.

## Prerequisites

Before you can run this application, you need to have the following installed:

- Python 3.6+
- Pip (Python package installer)

## Installation

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/chatbot-gui.git
   cd chatbot-gui

## Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install the required packages:
pip install -r requirements.txt

### Install python-dotenv to manage environment variables:
pip install python-dotenv
### Setup

## Obtain your OpenAI API key:
Sign up or log in to your OpenAI account and generate an API key from the OpenAI website.
Create a .env.local file:
In the root directory of the project, create a file named .env.local and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here
Your .env.local file should look like this:

### makefile
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Note about API usage:
If you encounter a "token exceeded" error, it means you've reached the usage limit of your API key. To increase the limit, you may need to add a payment method to your OpenAI account. Visit the OpenAI billing page to add a card and manage your usage.
Running the Application

### Run the application:

python main.py
File Structure

main.py: Contains the main application code for the GUI.
backend.py: Contains the backend logic for interacting with the OpenAI API.
.env.local: Environment file to store your OpenAI API key.
requirements.txt: Lists the dependencies required to run the application.
Usage

Input your message: Type your query in the text field and press "Send".
Receive the response: The chatbot will respond to your message using the OpenAI API and display it in the chat area.
