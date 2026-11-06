
import streamlit as st
import asyncio
from uuid import uuid4
from movie_backend import ask_movie

# Configure the webpage
st.set_page_config(
    page_title="Movie AI Assistant",
    page_icon="🎬",
    layout="centered"
)

# Display the title
st.title("🎬 Movie AI Assistant")

st.write(
    "Welcome! Ask me for movie recommendations "
    "or information about your favorite movies."
)

# Store messages between Streamlit reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Give each website visitor a unique conversation ID
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid4())

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Show the chat input
question = st.chat_input("Ask me about a movie...")

if question:
    # Display and save the user's question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Temporary response until we connect Ollama and MCP
    
    
    # Get a real answer from our Ollama + MCP agent
    with st.spinner("AI is thinking..."):
        answer = asyncio.run(
            ask_movie(
                question,
                st.session_state.thread_id
            )
        )



    # Display and save the response
    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
