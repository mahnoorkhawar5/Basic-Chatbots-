from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
llm=ChatMistralAI(model="mistral-small-2506")
message=[
   SystemMessage('You are Funny AI chatbot')
]
print ("------ WELCOME ------")
while True:
  
   prompt=input("You:")
   message.append(HumanMessage(content=prompt))
   if prompt == '0':
      break
   response= llm.invoke(message)
   message.append(AIMessage(content=response.content))
   print("Bot : ",response.content)

print(message)