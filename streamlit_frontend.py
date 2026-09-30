import uuid
import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot

# ***************************** Utility functions ************************************
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_chat(thread_id):
    return chatbot.get_state(config = {"configurable" : {"thread_id" : thread_id}}).values.get('messages', [])

# ***************************** Session Setup ************************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])

# ***************************** Sidebar UI ************************************

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads']: 
    if st.sidebar.button(thread_id):
        st.session_state['thread_id'] = thread_id
        messages = load_chat(thread_id)

        temp_messages = []

        for message in messages:
            if isinstance(message, HumanMessage):
                role = 'user'
                content = message.content
            else:
                role = 'assistant'
                content = message.content[0]["text"]

            temp_messages.append({'role' : role, 'content' : content})

        st.session_state['message_history'] = temp_messages

CONFIG = {"configurable" : {"thread_id" : st.session_state['thread_id']}}


# ***************************** Main UI ************************************

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type here ...")

if user_input:
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})

    with st.chat_message('user'):
        st.text(user_input)
    
    ai_reply = st.write_stream(
        message_chunk.content[0]["text"] 
        for message_chunk, metadata in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]}, config=CONFIG, stream_mode='messages'
        )
        if message_chunk.content and isinstance(message_chunk.content, list) and "text" in message_chunk.content[0]
    )

    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_reply})
