import streamlit as st

st.set_page_config(
    page_title="AI Citizen Fraud Shield",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Citizen Fraud Shield")
st.subheader("AI-Powered Detection and Prevention of Digital Arrest Scams")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🚨 **Module 1**\n\nScam Message Detector")

with col2:
    st.info("🔒 **Module 2**\n\nDigital Arrest Detector")

with col3:
    st.info("🤖 **Module 3**\n\nFraud Awareness Chatbot")

with col4:
    st.info("📊 **Module 4**\n\nFraud Intelligence Dashboard")

st.markdown("---")
st.markdown("**Use the sidebar to navigate between modules.**")
st.markdown("*ET AI Hackathon 2.0 | Problem #6 | Team: Shivani & Sreejani*")