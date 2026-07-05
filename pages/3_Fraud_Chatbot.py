import streamlit as st

st.set_page_config(page_title='Fraud Awareness Chatbot', page_icon='🤖')

st.title('🤖 AI Fraud Awareness Assistant')
st.write('Ask me anything about scams, digital arrests, or how to stay safe.')

# Fraud knowledge base
FRAUD_KNOWLEDGE = {
    'digital arrest': 'Digital Arrest is NOT a real legal concept in India. Real police never conduct arrests over video call. If someone claims to put you under digital arrest, it is 100% a scam. Hang up immediately and call 1930.',
    'cbi': 'Real CBI officers NEVER contact citizens over WhatsApp, Skype or video call. They never demand money for investigations. If someone claims to be CBI and asks for money, it is a scam.',
    'aadhaar': 'If someone says your Aadhaar is linked to a crime, do not panic. Real agencies send official written notices, never random phone calls. Verify by calling UIDAI helpline: 1947.',
    'otp': 'NEVER share OTP with anyone — not even someone claiming to be from your bank, RBI, or police. Real officials never ask for OTP.',
    'money transfer': 'No government agency, court, or police department will ever ask you to transfer money to clear your name or avoid arrest. This is always a scam.',
    'rbi': 'RBI never contacts individuals directly about their accounts. If someone claims to be from RBI and asks for money, it is a scam. Call RBI helpline: 14440.',
    'helpline': 'Cybercrime helpline: 1930. Report online: cybercrime.gov.in. UIDAI (Aadhaar): 1947. RBI: 14440. These are the ONLY official channels.',
}

def get_response(user_input):
    user_lower = user_input.lower()
    for keyword, response in FRAUD_KNOWLEDGE.items():
        if keyword in user_lower:
            return response
    # Default response
    return (
        "I'm here to help you identify scams and stay safe online. "
        "Here are key safety rules:\n\n"
        "🔴 Never share OTP with anyone\n"
        "🔴 Never transfer money to avoid 'arrest'\n"
        "🔴 Digital Arrest is NOT a real legal concept\n"
        "🔴 Real police never demand money over video call\n\n"
        "If you received a suspicious call, describe it to me and I'll help you identify if it's a scam.\n\n"
        "**Cybercrime Helpline: 1930**"
    )

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': '👋 Hello! I am SafeShield AI Assistant. I can help you identify scams and stay safe. Ask me anything about suspicious calls, messages, or digital arrest scams!'}
    ]

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# User input
if user_input := st.chat_input('Ask about a suspicious call or message...'):
    # Add user message
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)

    # Get and show response
    response = get_response(user_input)
    st.session_state.messages.append({'role': 'assistant', 'content': response})
    with st.chat_message('assistant'):
        st.markdown(response)