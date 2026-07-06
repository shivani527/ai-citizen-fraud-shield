import streamlit as st
import sys
sys.path.append('.')
from src.scam_detector import detect_scam

st.set_page_config(page_title='Digital Arrest Detector', page_icon='🔒')

st.title('🔒 Digital Arrest Detector')
st.write('Paste a suspicious call transcript, WhatsApp conversation, or message.')
st.info('💡 This module analyses call transcripts for digital arrest scam patterns using AI.')

transcript = st.text_area(
    'Paste call transcript or message:',
    placeholder='e.g. Caller: I am officer Sharma from CBI. Your Aadhaar number is linked to a money laundering case. You are under digital arrest...',
    height=250
)

if st.button('🔍 Detect Digital Arrest', type='primary') and transcript.strip():
    with st.spinner('Analysing for digital arrest patterns...'):
        result = detect_scam(transcript)

        # Advanced pattern analysis
        transcript_lower = transcript.lower()

        digital_arrest_patterns = {
            'Authority Impersonation': ['cbi', 'ed ', 'customs', 'police', 'cyber cell', 'rbi', 'income tax', 'ncb', 'enforcement directorate'],
            'Fear Tactics': ['arrest', 'warrant', 'fir', 'case filed', 'legal action', 'jail', 'prison', 'court notice'],
            'Digital Arrest': ['digital arrest', 'stay on call', 'do not disconnect', 'video call', 'stay connected', 'do not tell'],
            'Financial Demand': ['transfer money', 'send money', 'pay', 'escrow', 'verification amount', 'compliance', 'refundable'],
            'Urgency': ['immediately', 'right now', 'within 1 hour', 'last chance', 'final warning', 'tonight'],
            'Isolation': ['do not tell family', 'keep secret', 'confidential', 'do not contact', 'sub judice'],
        }

        found_patterns = {}
        for category, keywords in digital_arrest_patterns.items():
            found = [kw for kw in keywords if kw in transcript_lower]
            if found:
                found_patterns[category] = found

        total_categories = len(found_patterns)
        risk_score = min(total_categories * 18, 99)

        if total_categories >= 3:
            risk_level = 'CRITICAL'
            is_scam = True
        elif total_categories >= 2:
            risk_level = 'HIGH'
            is_scam = True
        elif total_categories >= 1:
            risk_level = 'MEDIUM'
            is_scam = result['is_scam']
        else:
            risk_level = 'LOW'
            is_scam = result['is_scam']

    # Display results
    if is_scam:
        if risk_level == 'CRITICAL':
            st.error('🚨 CRITICAL — DIGITAL ARREST SCAM DETECTED!')
        elif risk_level == 'HIGH':
            st.error('⚠️ HIGH RISK — DIGITAL ARREST PATTERNS FOUND!')
        else:
            st.warning('⚠️ MEDIUM RISK — Suspicious patterns detected')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Risk Level', risk_level)
        with col2:
            st.metric('Risk Score', f'{risk_score}/99')
        with col3:
            st.metric('Patterns Found', f'{total_categories}/6')

        st.progress(risk_score / 99)

        if found_patterns:
            st.subheader('🔴 Fraud Patterns Detected:')
            for category, keywords in found_patterns.items():
                with st.expander(f'🔴 {category} — {len(keywords)} indicator(s) found'):
                    for kw in keywords:
                        st.markdown(f'• **{kw}**')

        st.markdown("---")
        st.error('🚨 IMMEDIATE ACTION REQUIRED:')
        st.markdown("""
        - **STOP** — Do not transfer any money
        - **DISCONNECT** — End the call immediately  
        - **VERIFY** — Call the official agency directly
        - **REPORT** — Call **1930** (Cybercrime Helpline)
        - **TELL FAMILY** — Do not keep this secret
        """)
        st.info('⚠️ Remember: Digital Arrest is NOT a legal concept in India. Real CBI/Police NEVER demand money over video call.')

    else:
        st.success(f'✅ No digital arrest patterns detected — Risk Score: {risk_score}/99')
        st.info('Stay alert. If you feel something is suspicious, trust your instincts and call 1930.')

st.markdown("---")
st.markdown("📞 **Cybercrime Helpline: 1930** | 🌐 **cybercrime.gov.in**")