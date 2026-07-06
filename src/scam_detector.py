import streamlit as st
from transformers import pipeline
import os

SCAM_KEYWORDS = [
    'digital arrest', 'CBI', 'ED', 'Customs', 'Aadhaar misuse',
    'money laundering', 'arrest warrant', 'PMLA', 'non-bailable',
    'RBI escrow', 'compliance amount', 'stay on call',
    'do not disconnect', 'NCB', 'Income Tax investigation',
    'cyber crime department', 'freeze your account', 'legal action'
]

_classifier = None

@st.cache_resource
def load_classifier():
    global _classifier
    if _classifier is None:
        model_path = 'models/scam_model'
        if os.path.exists(model_path):
            print("Loading trained DistilBERT model...")
            _classifier = pipeline('text-classification',
                model=model_path, tokenizer=model_path)
        else:
            print("Trained model not found! Using base model...")
            _classifier = pipeline('text-classification',
                model='distilbert-base-uncased-finetuned-sst-2-english')
    return _classifier

def detect_scam(text: str) -> dict:
    clf = load_classifier()
    result = clf(text[:512])[0]
    is_scam = result['label'] == 'LABEL_1'
    confidence = round(result['score'] * 100, 1)
    red_flags = [kw for kw in SCAM_KEYWORDS if kw.lower() in text.lower()]

    if len(red_flags) >= 2:
        is_scam = True
        confidence = max(confidence, 88.0)

    risk = 'HIGH' if confidence > 85 else 'MEDIUM' if confidence > 60 else 'LOW'

    return {
        'is_scam':    is_scam,
        'label':      'SCAM' if is_scam else 'SAFE',
        'confidence': confidence,
        'risk_level': risk if is_scam else 'SAFE',
        'red_flags':  red_flags
    }