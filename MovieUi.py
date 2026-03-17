import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬", layout="centered")

st.title("🎬 Movie Info Extractor")
st.caption("Paste a movie paragraph and extract structured information using AI")

# ── LLM & Parser init ─────────────────────────────────────────────────────────
@st.cache_resource
def get_llm():
    return ChatMistralAI(model="mistral-small-2506")

LLM = get_llm()

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

message = ChatPromptTemplate.from_messages([
    ("system",
     """
     Extracr features of movie in {format_instructions}
"""),
    ("human",
     """
Extract information from this paragraph:
{paragraph}
""")
])

# ── UI ────────────────────────────────────────────────────────────────────────
para = st.text_area(
    "Provide the movie paragraph:",
    placeholder="e.g. The Dark Knight is a 2008 superhero film directed by Christopher Nolan...",
    height=180
)

if st.button("🔍 Extract Movie Info", use_container_width=True):
    if not para.strip():
        st.warning("Please enter a movie paragraph first.")
    else:
        with st.spinner("Extracting movie information..."):
            final_prompt = message.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            })
            response = LLM.invoke(final_prompt)
            movie_data = parser.parse(response.content)

        st.success("Extraction complete!")
        st.divider()
        st.subheader("📦 Extracted Movie Data")
        st.json(movie_data.model_dump())