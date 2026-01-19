import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from domain_classifier import predict_domain

st.title("Resume Analyzer using NLP")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    text = extract_text(uploaded_file)
    skills = extract_skills(text)
    domain = predict_domain(text)

    st.subheader("Extracted Skills")
    st.write(skills)

    st.subheader("Predicted Job Domain")
    st.success(domain)
