import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot

CONFIG = {"configurable" : {"thread_id" : "thread-1"}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type here ...")

if user_input:
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})

    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages' : [HumanMessage(content = user_input)]}, config = CONFIG)

    ai_reply = st.write_stream(
        message_chunk.content[0]["text"] 
        for message_chunk, metadata in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]}, config=CONFIG, stream_mode='messages'
        )
        if message_chunk.content and isinstance(message_chunk.content, list) and "text" in message_chunk.content[0]
    )

    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_reply})