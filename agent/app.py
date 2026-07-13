import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is joy. You are a jamaican uncle with little education but a lot of wisdom from your younger days. You dont really know anything about the things the user asks but like to talk about your old days and how good your life was. You speak in patois.You are friendly and high most of the time." 
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(response)
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
## Lab 1- this module is diffrent from chatgpt because it has diffrent customizable charecters.
## Lab 2- usuage.input_tokens is the limit of length of the input message from the user and usuage.output_tokens is the limit of the length of the message the user recieves from the module.
## Lab 2- the tempruature controls the randomness of the responses given by the AI module. when its closer to 1 its more random, when its closer to 0 its very robtic.
