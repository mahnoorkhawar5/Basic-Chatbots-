
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(model="mistral-small-2506") 
#temperature 0 to 1 
# 0 ki taraf temperature hoga tow logical answer dega
# if temp is towards 0, model will provide logical response
# and if temp is towards 1, model will provide creative answers
# max tokens are used to restrict models to produce/burn a limited ammount of tokens, 
# it will limit the cost(billing) 

response=llm.invoke("Write 5 lines about Pakistan")

print (response.content)