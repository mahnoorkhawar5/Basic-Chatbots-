import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Mood AI Chatbot", page_icon="🎭", layout="centered")

st.title("🎭 Mood AI Chatbot")
st.caption("Powered by Mistral · mistral-small-2506")

# ── LLM init ──────────────────────────────────────────────────────────────────
@st.cache_resource
def get_llm():
    return ChatMistralAI(model="mistral-small-2506", temperature=0.9)

model = get_llm()

# ── Mode selection (only if not chosen yet) ───────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = None  # not started yet
    st.session_state.mode_label = None

if st.session_state.messages is None:
    st.subheader("Choose your AI mode")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😠 Angry Mode", use_container_width=True):
            mode = "You are an angry AI agent. You respond aggressively and impatiently."
            st.session_state.mode_label = "😠 Angry Mode"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.rerun()
    with col2:
        if st.button("😂 Funny Mode", use_container_width=True):
            mode = "You are a very funny AI agent. You respond with humor and jokes."
            st.session_state.mode_label = "😂 Funny Mode"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.rerun()
    with col3:
        if st.button("😢 Sad Mode", use_container_width=True):
            mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
            st.session_state.mode_label = "😢 Sad Mode"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.rerun()

# ── Chat UI (after mode is selected) ─────────────────────────────────────────
else:
    st.info(f"Current mode: **{st.session_state.mode_label}**")

    # Reset button
    if st.button("🔄 Change Mode"):
        st.session_state.messages = None
        st.session_state.mode_label = None
        st.rerun()

    st.divider()

    # Display chat history
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # Input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.messages)
            st.write(response.content)

        st.session_state.messages.append(AIMessage(content=response.content))