import streamlit as st

st.set_page_config(
    page_title="AI Citizen Fraud Shield",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
div[role="alert"] * { color: white !important; }
.stat-box {
    background: linear-gradient(135deg, #185FA5, #0D2137);
    padding: 15px 10px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid #185FA5;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.stat-number {
    font-size: 26px;
    font-weight: bold;
    color: #FFD580;
    line-height: 1.2;
}
.stat-label {
    font-size: 11px;
    color: #B8D4EE;
    margin-top: 6px;
    line-height: 1.3;
}
.module-box {
    background: #1A3050;
    padding: 20px 15px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid #185FA5;
    min-height: 140px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🛡️ AI Citizen Fraud Shield")
st.subheader("AI-Powered Detection and Prevention of Digital Arrest Scams")
st.markdown("*ET AI Hackathon 2.0 | Problem #6 | Team: Shivani & Sreejani*")
st.markdown("---")

# Statistics Banner
st.markdown("### 📊 India Cybercrime — Key Statistics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">1.14M</div>
        <div class="stat-label">Cybercrime complaints 2023</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">₹1,776Cr</div>
        <div class="stat-label">Lost to Digital Arrest scams</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">60%</div>
        <div class="stat-label">Year-on-year crime increase</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">52,974</div>
        <div class="stat-label">Cases reported in 2021</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">1930</div>
        <div class="stat-label">Cybercrime Helpline 24/7</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4 Module Cards
st.markdown("### 🤖 Our AI Modules")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="module-box">
        <h3 style="color:white; font-size:15px; margin:0;">🚨 Module 1</h3>
        <p style="color:white; font-size:13px; margin:6px 0;">Scam Message Detector</p>
        <p style="color:#B8D4EE; font-size:11px; margin:0;">DistilBERT AI — detects SMS, WhatsApp & email scams</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-box">
        <h3 style="color:white; font-size:15px; margin:0;">🔒 Module 2</h3>
        <p style="color:white; font-size:13px; margin:6px 0;">Digital Arrest Detector</p>
        <p style="color:#B8D4EE; font-size:11px; margin:0;">AI pattern analysis — detects digital arrest scam scripts</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="module-box">
        <h3 style="color:white; font-size:15px; margin:0;">🤖 Module 3</h3>
        <p style="color:white; font-size:13px; margin:6px 0;">Fraud Awareness Chatbot</p>
        <p style="color:#B8D4EE; font-size:11px; margin:0;">AI assistant — answers all fraud awareness questions</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="module-box">
        <h3 style="color:white; font-size:15px; margin:0;">📊 Module 4</h3>
        <p style="color:white; font-size:13px; margin:6px 0;">Fraud Intelligence Dashboard</p>
        <p style="color:#B8D4EE; font-size:11px; margin:0;">NCRB data — India cybercrime trends & hotspots</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Alert Banner
st.error("🚨 **ALERT:** Digital Arrest is NOT a legal concept in India. Real CBI/Police NEVER demand money over video call. If you receive such a call — **HANG UP and call 1930 immediately!**")

st.markdown("---")

# How to use
st.markdown("### 👈 How to use SafeShield AI")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("**Step 1**\n\nPaste any suspicious message in Scam Detector")
with c2:
    st.info("**Step 2**\n\nGet instant AI analysis with risk score and red flags")
with c3:
    
    st.info("**Step 3**\n\nCall **1930** to report if scam is detected")

st.markdown("---")
st.markdown("📞 **Cybercrime Helpline: 1930** | 🌐 **cybercrime.gov.in** | *Data Source: NCRB, MHA India*")