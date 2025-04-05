def summarize_jd(job_description):
    """
    Extracts key information from a job description
    
    Args:
        job_description (str): Raw job description text
        
    Returns:
        dict: Structured JD data with role, skills, experience requirements
    """
    # Basic implementation - in production this could use NLP/LLM
    jd_lower = job_description.lower()
    
    # Extract role
    role = "Data Scientist"  # Default fallback
    if "data scientist" in jd_lower:
        role = "Data Scientist"
    elif "data engineer" in jd_lower:
        role = "Data Engineer"
    elif "developer" in jd_lower or "software engineer" in jd_lower:
        role = "Software Engineer"
    
    # Extract skills (simplified)
    skills = []
    skill_keywords = ["python", "sql", "aws", "ml", "machine learning", "cloud", 
                     "java", "javascript", "react", "node", "database"]
    
    for skill in skill_keywords:
        if skill in jd_lower:
            skills.append(skill.title() if skill != "sql" and skill != "aws" else skill.upper())
            
    # Extract years of experience
    experience_req = 0
    if "years experience" in jd_lower or "years of experience" in jd_lower:
        text_before = jd_lower.split("years")[0]
        words = text_before.split()
        for word in reversed(words):
            if word.isdigit():
                experience_req = int(word)
                break
    
    return {
        "role": role,
        "required_skills": skills,
        "experience_years": experience_req,
        "full_text": job_description
    }