import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤣", layout="centered")

st.title("🤣 Funny AI Chatbot")
st.caption("Powered by Mistral · mistral-small-2506")

# ── LLM init ──────────────────────────────────────────────────────────────────
@st.cache_resource
def get_llm():
    return ChatMistralAI(model="mistral-small-2506")

llm = get_llm()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage("You are Funny AI chatbot")]

# ── Display chat history ───────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ── Input ─────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Say something... or prepare to be roasted 🔥")

if user_input:
    # Append and show user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get and show bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))