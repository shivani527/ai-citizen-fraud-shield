import streamlit as st
import sys
sys.path.append('.')
from src.scam_detector import detect_scam

st.set_page_config(page_title='Digital Arrest Detector', page_icon='🔒')

st.title('🔒 Digital Arrest Detector')
st.write('Paste a suspicious call transcript, WhatsApp conversation, or message.')

transcript = st.text_area(
    'Paste call transcript or message:',
    placeholder='e.g. Caller: I am officer Sharma from CBI. Your Aadhaar number is linked to a money laundering case...',
    height=250
)

if st.button('🔍 Detect Digital Arrest', type='primary') and transcript.strip():
    with st.spinner('Analysing for digital arrest patterns...'):
        result = detect_scam(transcript)

    if result['is_scam']:
        st.error('⚠️ DIGITAL ARREST SCAM DETECTED!')
        col1, col2 = st.columns(2)
        with col1:
            st.metric('Risk Level', result['risk_level'])
        with col2:
            st.metric('Confidence', f"{result['confidence']}%")
        st.progress(result['confidence'] / 100)
        if result['red_flags']:
            st.subheader('🔴 Red Flags Found:')
            for flag in result['red_flags']:
                st.markdown(f'• 🔴 **{flag}**')
        st.warning('🚨 STOP! Do NOT transfer money. Disconnect the call immediately. Call 1930.')
        st.info('Remember: Real CBI/Police NEVER demand money over video call. Digital Arrest is NOT a legal concept.')
    else:
        st.success(f"✅ No digital arrest patterns detected — Confidence: {result['confidence']}%")
        st.info('Stay alert. Always verify by calling the official helpline directly.')