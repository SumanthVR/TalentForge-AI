import sys
import os

# Ensure current working directory is in the path to allow relative imports
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from agents.jd_summarizer import summarize_jd
from agents.resume_parser import parse_resume
from agents.matching_agent import calculate_match_score
from agents.interview_scheduler import schedule_interview
from agents.db_operations import save_all_to_db

# ------------------------------ 
# 🚀 Sample Inputs
# ------------------------------ 
sample_jd = """
Looking for a Data Scientist with experience in Python, ML, and cloud platforms.
Minimum 3 years experience. Must know SQL and be familiar with AWS.
"""

sample_resume = {
    "name": "Alyssa Chavez",
    "email": "alyssachavez88@gmail.com",
    "experience": "Data Scientist at ABC Inc. (2019-2023)",
    "skills": ["Python", "Machine Learning", "AWS", "SQL"],
    "certifications": ["AWS Certified Solutions Architect"],
    "education": "Diploma in Software Engineering"
}

# ------------------------------ 
# 🧠 Execution Pipeline
# ------------------------------ 
print("🔍 Summarizing Job Description...")
jd_data = summarize_jd(sample_jd)
print("✅ JD Summary:", jd_data)

print("\n📄 Parsing Candidate Resume...")
resume_data = parse_resume(sample_resume)
print("✅ Resume Data:", resume_data)

print("\n📊 Calculating Match Score...")
match_score = calculate_match_score(jd_data, resume_data)
print(f"✅ Match Score: {match_score}%")

print("\n📅 Scheduling Interview...")
email_content = schedule_interview(resume_data['name'], resume_data['email'], match_score)
print("✅ Email Content:\n", email_content)

print("\n💾 Saving to Database...")
save_all_to_db(jd_data, resume_data, match_score, email_content)

print("\n🎉 --- DEMO COMPLETED ---")