from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()
LLM=ChatMistralAI(model="mistral-small-2506")
class Movie(BaseModel):
    title: str 
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str
    
parser=PydanticOutputParser(pydantic_object=Movie)


message=ChatPromptTemplate.from_messages([
    ("system",
     """
     Extracr features of movie in {format_instructions}
"""
),
(
    'human',
    """
Extract information from this paragraph:
{paragraph}
"""
)
]
)

para=input("Provide the movive paragraph:")
final_prompt=message.invoke(
    {"paragraph": para,
    "format_instructions": parser.get_format_instructions()
    }
)
response=LLM.invoke(
    final_prompt
)
movie_data = parser.parse(response.content)
print(movie_data)
