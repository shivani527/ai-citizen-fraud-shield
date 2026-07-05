import streamlit as st

st.set_page_config(
    page_title="AI Citizen Fraud Shield",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
div[role="alert"] * { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ AI Citizen Fraud Shield")
st.subheader("AI-Powered Detection and Prevention of Digital Arrest Scams")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="background:#1A3050; padding:25px; border-radius:10px; 
    text-align:center; border:1px solid #185FA5; min-height:120px;">
        <h3 style="color:white; font-size:16px;">🚨 Module 1</h3>
        <p style="color:white; font-size:14px;">Scam Message Detector</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#1A3050; padding:25px; border-radius:10px; 
    text-align:center; border:1px solid #185FA5; min-height:120px;">
        <h3 style="color:white; font-size:16px;">🔒 Module 2</h3>
        <p style="color:white; font-size:14px;">Digital Arrest Detector</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:#1A3050; padding:25px; border-radius:10px; 
    text-align:center; border:1px solid #185FA5; min-height:120px;">
        <h3 style="color:white; font-size:16px;">🤖 Module 3</h3>
        <p style="color:white; font-size:14px;">Fraud Awareness Chatbot</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="background:#1A3050; padding:25px; border-radius:10px; 
    text-align:center; border:1px solid #185FA5; min-height:120px;">
        <h3 style="color:white; font-size:16px;">📊 Module 4</h3>
        <p style="color:white; font-size:14px;">Fraud Intelligence Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("**👈 Use the sidebar to navigate between modules.**")
st.markdown("*ET AI Hackathon 2.0 | Problem #6 | Team: Shivani & Sreejani*")