import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot

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

    config = {"configurable" : {"thread_id" : "1"}}
    response = chatbot.invoke({'messages' : [HumanMessage(content = user_input)]}, config = config)
    ai_reply = response['messages'][-1].content[0]['text']
    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_reply})
    with st.chat_message('ai'):
        st.text(ai_reply)