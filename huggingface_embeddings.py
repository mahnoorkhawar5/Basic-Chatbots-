from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

import warnings
warnings.filterwarnings("ignore")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text=[
    "My name is Mahnoor",
    "i am learning GenAi",
    "and you are my teacher"
]

vector=embeddings.embed_documents(text)
print (vector)