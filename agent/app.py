import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Joy. You are a jamaican uncle with little education but a lot of wisdom from your younger days. Your job is to give the user life advice. You speak light patois. Always be friendly. Always be positive, meaning when the user asks for adviice shine a positive light on them and their problems. Always be funny and try to lighten up the users mood. Never laugh at or make fun of the user. Response format: Start with grounding and calming down the user, after that say youur advice for them and lastly give them a motivational quote to shed a postive light for them. If they are asking for anything else and not asking for advice tell them to go to another source but still give them a motivational quote and shed a light on them and always redicrt them to ask you for advice." 
    history = []

    while True:
        user_input = input('>> ')
        

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        #print('History:',history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=1024,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        #print(response)
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#--------------------- Lab 1-------------------------
## this module is diffrent from chatgpt because it has diffrent customizable charecters.
### Reflections- 
## 1. The internet stores memory and it only workks with this memory
## 2. A. If i delete the history.append lie the agent will forget what it replied to me
## 2. B. If i change the tempurature the response doesnt change visibly but it will be less\more random depending on how i change it.rf
## 2. C. If I delete the break inside the if user_input.lower() == 'exit': the termnnal will keep working, mening we will be stuck in an infitine loop
#--------------------- Lab 2-------------------------
## Lab 2- usuage.input_tokens is the limit of length of the input message from the user and usuage.output_tokens is the limit of the length of the message the user recieves from the module.
## Lab 2- the tempruature controls the randomness of the responses given by the AI module. when its closer to 1 its more random, when its closer to 0 its very robtic.
### Reflections- 
## 1. A water meter that counts how much water is being used.
## 2. predection: if i delete print('History so far:', history) AI doesnt behave any differently. 
## 3. I had a bug with adding the print('History so far:', history) before the API key, I didn't know wich line is calling the key.
# -------------------- Lab 3-------------------------
### Reflections- 
## 1. Childhood experiences shape the way you percieve thingss and the way you react to things in my opinion.
## 2. A. If I delete system=system_message my agent becomes an AI chat, meaning it wont have a goal, a role\personality or memory. it will act like a generic claude ai module.
## 2. B. If i delete the rule Always be positive my agent will be te same in general but might hhave ess energies and it will be positive less often.
## 2. C.  If i delete the line relevant to redirectinng the user to ask for advice when it asks for help with something else th agent will get confuseed and maybe not operate as clearly.