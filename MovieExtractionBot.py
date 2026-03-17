from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
message=ChatPromptTemplate.from_messages([
    ("system",
"""
You are an AI assistant specialized in extracting useful information from movie descriptions.

Task:
1. Read the paragraph below.
2. Extract the following information and present it in **plain text**:
   - Movie Name
   - Genre
   - Director
   - Release Year
   - Main Cast
   - IMDb Rating (if available)
   - Key Plot Points (1-2 lines)
   - Soundtrack / Composer (if mentioned)
3. Provide a 2-3 sentence **summary** of the paragraph.

Instructions:
- Present each field clearly with a label.
- Write the summary in natural, readable language.
- Do NOT use JSON or any code format.

Short Summary:
"""),
(

    'human',
    """
Extract information from this paragraph:
{paragraph}
"""
)
]
)

LLM=ChatMistralAI(model="mistral-small-2506")

para=input("Provide the movive paragraph:")
final_prompt=message.invoke(
    {"paragraph": para}
)
response=LLM.invoke(
    final_prompt
)
print (response.content)
