import streamlit as st
from agents.jd_summarizer import summarize_jd
from agents.resume_parser import parse_resume
from agents.matching_agent import calculate_match_score
from agents.interview_scheduler import schedule_interview
from agents.db_operations import save_all_to_db

st.title("🧠 TalentForge AI - Resume Matcher")

# --- JD input with predefined example ---
default_jd = """Looking for a Data Scientist with experience in Python, ML, and cloud platforms.
Minimum 3 years experience. Must know SQL and be familiar with AWS.
Responsibilities include building predictive models and collaborating with cross-functional teams."""

jd_text = st.text_area("📄 Paste Job Description", value=default_jd, height=150)

# --- Resume input ---
st.subheader("👤 Candidate Resume Info")
name = st.text_input("Name")
email = st.text_input("Email")
skills = st.text_input("Skills (comma-separated)")
experience = st.text_area("Experience")
certifications = st.text_input("Certifications (comma-separated)")
education = st.text_input("Education")

if st.button("⚙️ Run Matching"):
    if jd_text and name and email:
        jd_data = summarize_jd(jd_text)
        resume_data = {
            "name": name,
            "email": email,
            "experience": experience,
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "certifications": [c.strip() for c in certifications.split(",") if c.strip()],
            "education": education
        }
        parsed_resume = parse_resume(resume_data)
        match_score = calculate_match_score(jd_data, parsed_resume)
        email_msg = schedule_interview(name, email, match_score)
        save_all_to_db(jd_data, parsed_resume, match_score, email_msg)
        
        st.success(f"✅ Match Score: {match_score}%")
        st.info("📧 Email Message:")
        st.code(email_msg)
    else:
        st.warning("Please fill all required fields.")