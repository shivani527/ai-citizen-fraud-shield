import streamlit as st

st.set_page_config(page_title='Fraud Awareness Chatbot', page_icon='🤖')

st.title('🤖 AI Fraud Awareness Assistant')
st.write('Ask me anything about scams, digital arrests, or how to stay safe.')

FRAUD_KNOWLEDGE = {
    'digital arrest': {
        'answer': """**Digital Arrest is 100% FAKE — It does not exist in Indian law!**

🔴 What scammers do:
- Impersonate CBI, ED, Police, Customs, RBI officers
- Call you on WhatsApp/Skype claiming you are "under digital arrest"
- Force you to stay on video call for hours
- Threaten arrest, account freeze, passport cancellation
- Demand money to "clear your name"

✅ The truth:
- No Indian law allows arrest over a phone or video call
- Real government agencies NEVER contact citizens this way
- Real officers NEVER demand money for investigations
- This is a psychological trap designed to create panic

🛡️ What to do:
1. **HANG UP immediately**
2. **Do NOT transfer any money**
3. **Tell your family** — scammers say keep it secret, that's a red flag
4. **Call 1930** — National Cybercrime Helpline
5. **Report at** cybercrime.gov.in

📞 Remember: Prime Minister Modi himself warned citizens about digital arrest scams in his Mann Ki Baat address."""
    },

    'cbi': {
        'answer': """**Fake CBI calls are one of the most common digital arrest scams!**

🔴 How fake CBI scams work:
- Caller claims to be "CBI Officer" or "CBI Director"
- Shows fake ID cards on video call
- Claims your Aadhaar/PAN is linked to a criminal case
- Threatens arrest within 1-2 hours
- Demands money as "bail" or "verification fee"

✅ The truth about real CBI:
- Real CBI NEVER contacts citizens via WhatsApp or random calls
- Real CBI sends official written summons through proper legal channels
- Real CBI NEVER demands money over phone
- Real CBI does not conduct "digital arrests"

🛡️ What to do immediately:
1. Ask for their official ID and case number
2. Hang up and call CBI headquarters directly: 011-24363006
3. Do NOT share any personal or banking details
4. Call 1930 to report the scam""",
    },

    'aadhaar': {
        'answer': """**Aadhaar misuse scams are designed to create panic and fear!**

🔴 Common Aadhaar scam claims:
- "Your Aadhaar is linked to 15 illegal SIM cards"
- "Your Aadhaar was used in drug trafficking"
- "Your Aadhaar is connected to a money laundering case"
- "We need to verify your Aadhaar to clear your name"

✅ The truth:
- UIDAI (Aadhaar authority) NEVER calls citizens about misuse
- Real agencies send official written notices, never random calls
- You can check your Aadhaar usage yourself online
- No one can "link" your Aadhaar to crimes without your knowledge

🛡️ What to do:
1. **Do NOT panic** — this is a psychological manipulation tactic
2. **Check your Aadhaar history** at myaadhaar.uidai.gov.in
3. **Lock your Aadhaar biometrics** at myaadhaar.uidai.gov.in
4. **Call UIDAI helpline: 1947** to report misuse
5. **Never share your Aadhaar OTP** with anyone""",
    },

    'otp': {
        'answer': """**NEVER share OTP with ANYONE — this is the golden rule of digital safety!**

🔴 Who asks for OTP in scams:
- Fake bank customer care agents
- Fake RBI officers
- Fake CBI/police officers  
- Fake telecom company agents
- Fake KYC verification callers

✅ The truth about OTP:
- OTP = One Time Password — it is YOUR private key
- Banks clearly state: "We will NEVER ask for your OTP"
- Sharing OTP = giving full access to your account
- Once shared, money can be transferred within seconds

🔴 Common OTP scam tricks:
- "We need OTP to verify your KYC"
- "Share OTP to unfreeze your account"  
- "OTP needed to process your refund"
- "Share OTP to complete police verification"

🛡️ Remember:
- No genuine organisation ever needs your OTP
- End the call IMMEDIATELY if anyone asks for OTP
- Call your bank's official helpline if worried about your account""",
    },

    'upi': {
        'answer': """**UPI fraud is the fastest growing cybercrime in India!**

🔴 Common UPI fraud tricks:
- **Collect request scam**: Scammer sends a COLLECT request — you approve thinking it's a payment TO you, but money goes FROM you
- **Fake QR code**: Scammer sends QR code saying "scan to receive money" — but QR codes only SEND money, never receive
- **Screen sharing scam**: Scammer asks you to share screen, then initiates UPI transaction
- **Fake UPI handle**: Creates handles like @sbi.support or @paytm.help to look official

✅ The truth about UPI:
- You NEVER need to enter PIN to RECEIVE money
- Scanning QR code = SENDING money, not receiving
- Entering PIN always means money LEAVES your account
- Real banks never ask for UPI PIN

🛡️ Safety rules:
1. Never enter UPI PIN to "receive" money — that's impossible
2. Never scan QR codes from unknown sources
3. Verify the recipient's name before confirming payment
4. Call 1930 immediately if you are scammed""",
    },

    'rbi': {
        'answer': """**Fake RBI calls are used to steal money and banking credentials!**

🔴 Fake RBI scam claims:
- "RBI has frozen your account due to suspicious transactions"
- "Your account will be blocked — verify immediately"
- "RBI is upgrading KYC — share your details"
- "Transfer money to RBI escrow account for verification"

✅ The truth about RBI:
- RBI is a regulatory body — it does NOT directly contact individual customers
- RBI NEVER asks for money transfers
- RBI NEVER asks for your account details or OTP
- RBI NEVER freezes individual accounts directly

🛡️ What to do:
1. Hang up immediately on any "RBI caller"
2. Contact your bank directly using the number on the back of your card
3. Check RBI official website: rbi.org.in
4. Call RBI helpline: 14440
5. Report the scam at 1930""",
    },

    'kyc': {
        'answer': """**Fake KYC update scams trick you into giving full account access!**

🔴 How KYC scams work:
- Get a call/SMS saying "Your KYC is expired, account will be blocked"
- Sent a link to a fake banking website
- Asked to enter account number, password, OTP
- Scammer gets full access and transfers all money

✅ The truth about KYC:
- Real KYC updates happen at bank branches or official bank apps
- Banks send official letters or notifications through registered email/SMS
- No bank calls randomly asking for credentials
- A bank NEVER asks for your password or full OTP

🛡️ How to check real KYC status:
1. Log in to your official bank app or website
2. Visit your nearest bank branch with original documents
3. Call the official customer care number on bank's website
4. NEVER click links in SMS/WhatsApp for KYC updates""",
    },

    'helpline': {
        'answer': """**Official Cybercrime Helplines in India — Save these numbers!**

🚨 **IMMEDIATE HELP:**
- **1930** — National Cybercrime Helpline (24/7)
- **cybercrime.gov.in** — Online complaint portal

🏛️ **Government Helplines:**
- **UIDAI (Aadhaar):** 1947
- **RBI Banking Ombudsman:** 14440  
- **CBI Headquarters:** 011-24363006
- **National Emergency:** 112

📱 **Telecom Fraud:**
- **TRAI (SIM fraud):** 1800-110-420
- **Sanchar Saathi (lost phone):** sancharsaathi.gov.in

🏦 **Banking Fraud:**
- **SBI:** 1800-11-2211
- **HDFC:** 1800-202-6161
- **ICICI:** 1800-1080
- **Axis Bank:** 1800-419-5959

⚡ **Act within GOLDEN HOUR:**
If you have been scammed, call 1930 within 1 hour — banks can freeze the transaction and recover your money!""",
    },

    'phishing': {
        'answer': """**Phishing attacks trick you into giving away passwords and banking details!**

🔴 Types of phishing in India:
- **SMS phishing (Smishing)**: Fake SMS with malicious links
- **Email phishing**: Fake emails from "your bank" or "government"
- **WhatsApp phishing**: Fake job offers, lottery wins, KYC links
- **Call phishing (Vishing)**: Fake customer care calls

🔴 Warning signs of phishing:
- Link looks similar but slightly different (sbi-bank.com instead of sbi.co.in)
- Creates urgency: "Act in 2 hours or account blocked"
- Asks for password, OTP, card number
- Offers that seem too good to be true

✅ How to stay safe:
1. Never click links in SMS or WhatsApp for banking
2. Always type bank URL directly in browser
3. Check for https:// and padlock icon
4. Use official bank apps downloaded from Play Store/App Store
5. Enable 2-factor authentication on all accounts

🛡️ Report phishing:
- Forward phishing SMS to 1909
- Report to cybercrime.gov.in""",
    },

    'investment': {
        'answer': """**Investment frauds have stolen thousands of crores from Indians!**

🔴 Common investment scam types:
- **Fake stock tips**: WhatsApp groups promising 300% returns
- **Ponzi schemes**: "Invest Rs 10,000, get Rs 1 lakh in 30 days"
- **Fake trading apps**: Apps that show fake profits but steal money
- **Cryptocurrency scams**: Fake crypto exchanges and mining schemes
- **MLM fraud**: Pyramid schemes disguised as business opportunities

🔴 Red flags:
- Guaranteed high returns (anything above 12% is suspicious)
- Pressure to invest quickly
- No proper registration or SEBI approval
- Cannot withdraw your money easily
- Recruiter is a random WhatsApp contact

✅ Before investing always check:
1. Is the company SEBI registered? Check at sebi.gov.in
2. Is the broker registered? Check at NSE/BSE websites
3. Never invest based on WhatsApp tips
4. If it sounds too good to be true — it IS a scam

🛡️ Report investment fraud:
- SEBI helpline: 1800-22-7575
- cybercrime.gov.in""",
    },
}

def get_response(user_input):
    user_lower = user_input.lower()
    
    # Check each keyword
    for keyword, data in FRAUD_KNOWLEDGE.items():
        if keyword in user_lower:
            return data['answer']
    
    # Check for related words
    if any(w in user_lower for w in ['safe', 'protect', 'safety', 'tips', 'advice']):
        return """**Top 10 Rules to Stay Safe from Cyber Fraud:**

1. 🔴 **Never share OTP** with anyone — ever
2. 🔴 **Digital Arrest is fake** — hang up immediately
3. 🔴 **Real police never demand money** over phone/video call
4. 🔴 **Never scan QR codes** to "receive" money
5. 🔴 **Never click links** in SMS/WhatsApp for banking
6. 🔴 **Never share screen** with unknown callers
7. ✅ **Always verify** by calling official numbers directly
8. ✅ **Tell your family** if you get suspicious calls
9. ✅ **Save 1930** — National Cybercrime Helpline
10. ✅ **Report immediately** at cybercrime.gov.in

💡 **Golden Rule:** If someone creates PANIC and asks for MONEY — it is always a SCAM!"""

    if any(w in user_lower for w in ['hello', 'hi', 'hey', 'namaste']):
        return """👋 **Hello! I am SafeShield AI Assistant!**
        
I can help you with:
- 🔍 **Digital Arrest Scams** — What they are and how to avoid them
- 💳 **UPI Frauds** — How to stay safe with online payments  
- 🏦 **Fake Bank/RBI calls** — How to identify and report them
- 📱 **KYC Scams** — What to do if you get fake KYC calls
- 🔐 **OTP Safety** — Why you should never share OTP
- 📈 **Investment Frauds** — How to identify fake schemes
- 📞 **Helplines** — All official numbers to report cybercrime

Just ask me anything! For example:
- "What is digital arrest?"
- "Someone called claiming to be CBI, what should I do?"
- "Is this UPI transaction safe?"
- "What are the cybercrime helpline numbers?" """

    if any(w in user_lower for w in ['scam', 'fraud', 'cheat', 'fake', 'suspicious', 'call']):
        return """🚨 **If you received a suspicious call or message:**

**IMMEDIATE STEPS:**
1. **Stay calm** — scammers want you to panic
2. **Do NOT transfer money** under any circumstances
3. **Do NOT share OTP, password, or bank details**
4. **Hang up** if on call — you have the right to disconnect
5. **Tell a trusted family member** immediately

**HOW TO VERIFY:**
- Note the caller's name and agency they claimed
- Call the OFFICIAL number of that agency directly
- Never call back on the number they gave you

**HOW TO REPORT:**
- 📞 Call **1930** — National Cybercrime Helpline
- 🌐 Report at **cybercrime.gov.in**
- 🏛️ Visit your nearest police station

**Remember:** Acting fast within the GOLDEN HOUR (first 60 minutes) can help recover your money!"""

    return """I can help you with fraud awareness! Here are topics I know about:

🔍 Type any of these to get detailed information:
- **"digital arrest"** — Most common scam in India right now
- **"CBI scam"** — Fake officer impersonation
- **"Aadhaar misuse"** — Fake Aadhaar linked to crime claims  
- **"OTP safety"** — Why never to share OTP
- **"UPI fraud"** — Online payment scams
- **"RBI scam"** — Fake RBI officer calls
- **"KYC scam"** — Fake KYC update calls
- **"phishing"** — Fake websites and links
- **"investment fraud"** — Fake trading and Ponzi schemes
- **"helpline"** — All official cybercrime helpline numbers

📞 **Emergency: Call 1930 if you have been scammed!**"""

# Initialize chat
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': """👋 **Hello! I am SafeShield AI Assistant!**

I can help you identify scams and stay safe online. Ask me about:
- Digital Arrest Scams
- UPI Frauds  
- Fake CBI/RBI calls
- OTP Safety
- KYC Scams
- Investment Frauds

📞 **Emergency Helpline: 1930**"""}
    ]

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Quick question buttons
st.markdown("**Quick questions:**")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('What is digital arrest?'):
        question = 'What is digital arrest?'
        st.session_state.messages.append({'role':'user','content':question})
        response = get_response(question)
        st.session_state.messages.append({'role':'assistant','content':response})
        st.rerun()
with col2:
    if st.button('UPI fraud tips'):
        question = 'UPI fraud tips'
        st.session_state.messages.append({'role':'user','content':question})
        response = get_response(question)
        st.session_state.messages.append({'role':'assistant','content':response})
        st.rerun()
with col3:
    if st.button('Helpline numbers'):
        question = 'helpline numbers'
        st.session_state.messages.append({'role':'user','content':question})
        response = get_response(question)
        st.session_state.messages.append({'role':'assistant','content':response})
        st.rerun()
with col4:
    if st.button('OTP safety'):
        question = 'OTP safety'
        st.session_state.messages.append({'role':'user','content':question})
        response = get_response(question)
        st.session_state.messages.append({'role':'assistant','content':response})
        st.rerun()

# User input
if user_input := st.chat_input('Ask about a suspicious call or message...'):
    st.session_state.messages.append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.markdown(user_input)
    response = get_response(user_input)
    st.session_state.messages.append({'role':'assistant','content':response})
    with st.chat_message('assistant'):
        st.markdown(response)

st.markdown("---")
st.markdown("📞 **Cybercrime Helpline: 1930** | 🌐 **cybercrime.gov.in**")