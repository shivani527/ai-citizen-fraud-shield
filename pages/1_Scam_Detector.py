import streamlit as st
import sys
sys.path.append('.')
from src.scam_detector import detect_scam

st.set_page_config(page_title='Scam Detector', page_icon='🚨')

st.title('🚨 Scam Message Detector')
st.write('Paste any suspicious SMS, WhatsApp, or email message below.')

text = st.text_area(
    'Paste suspicious message here:',
    placeholder='e.g. This is CBI officer. Your Aadhaar is linked to money laundering...',
    height=200
)

if st.button('🔍 Analyse Message', type='primary') and text.strip():
    with st.spinner('Analysing...'):
        result = detect_scam(text)

    if result['is_scam']:
        st.error(f"🚨 {result['label']} DETECTED — Confidence: {result['confidence']}%")
        st.metric('Risk Level', result['risk_level'])
        st.progress(result['confidence'] / 100)
        if result['red_flags']:
            st.subheader('🔴 Red Flags Found:')
            for flag in result['red_flags']:
                st.markdown(f'• 🔴 **{flag}**')
        st.warning('⚠️ Do NOT transfer money or share OTP. Call 1930 (Cybercrime Helpline).')
    else:
        st.success(f"✅ Message appears SAFE — Confidence: {result['confidence']}%")