import sqlite3
import json
import os
from datetime import datetime

def save_all_to_db(jd_data, resume_data, match_score, email_content):
    """
    Save all processed data to SQLite database
    
    Args:
        jd_data (dict): Processed job description data
        resume_data (dict): Processed resume data
        match_score (int): Calculated match percentage
        email_content (str): Generated email content
    """
    db_path = 'talentforge.db'
    
    # Create database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path) if os.path.dirname(db_path) else '.', exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_descriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        required_skills TEXT,
        experience_years INTEGER,
        full_text TEXT,
        created_at TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        skills TEXT, 
        experience TEXT,
        certifications TEXT,
        education TEXT,
        years_experience INTEGER,
        created_at TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        candidate_id INTEGER,
        match_score INTEGER,
        email_content TEXT,
        created_at TEXT,
        FOREIGN KEY (job_id) REFERENCES job_descriptions (id),
        FOREIGN KEY (candidate_id) REFERENCES candidates (id)
    )
    ''')
    
    # Insert job description
    now = datetime.now().isoformat()
    
    cursor.execute(
        'INSERT INTO job_descriptions (role, required_skills, experience_years, full_text, created_at) VALUES (?, ?, ?, ?, ?)',
        (
            jd_data.get('role', ''),
            json.dumps(jd_data.get('required_skills', [])),
            jd_data.get('experience_years', 0),
            jd_data.get('full_text', ''),
            now
        )
    )
    job_id = cursor.lastrowid
    
    # Insert candidate
    cursor.execute(
        'INSERT INTO candidates (name, email, skills, experience, certifications, education, years_experience, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (
            resume_data.get('name', ''),
            resume_data.get('email', ''),
            json.dumps(resume_data.get('skills', [])),
            resume_data.get('experience', ''),
            json.dumps(resume_data.get('certifications', [])),
            resume_data.get('education', ''),
            resume_data.get('years_experience', 0),
            now
        )
    )
    candidate_id = cursor.lastrowid
    
    # Insert match record
    cursor.execute(
        'INSERT INTO matches (job_id, candidate_id, match_score, email_content, created_at) VALUES (?, ?, ?, ?, ?)',
        (job_id, candidate_id, match_score, email_content, now)
    )
    
    # Commit and close connection
    conn.commit()
    conn.close()