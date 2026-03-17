from dotenv import load_dotenv

load_dotenv()
# For chat-style LLM
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

llm= HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

llm=ChatHuggingFace(llm=llm)

responce=llm.invoke("Name 5 Cricket Players")
print(responce.content)