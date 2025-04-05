def calculate_match_score(jd_data, resume_data):
    """
    Calculate match percentage between job requirements and candidate
    
    Args:
        jd_data (dict): Processed job description data
        resume_data (dict): Processed resume data
        
    Returns:
        int: Match percentage (0-100)
    """
    score = 0
    total_points = 0
    
    # Skills match (50% of total score)
    required_skills = [s.lower() for s in jd_data.get('required_skills', [])]
    candidate_skills = [s.lower() for s in resume_data.get('skills', [])]
    
    skill_points = 50
    total_points += skill_points
    
    if required_skills:
        matched_skills = sum(1 for skill in required_skills if skill in candidate_skills)
        score += (matched_skills / len(required_skills)) * skill_points
    else:
        # If no skills specified in JD, grant partial points
        score += skill_points * 0.5
    
    # Experience match (30% of total score)
    exp_points = 30
    total_points += exp_points
    
    required_years = jd_data.get('experience_years', 0)
    candidate_years = resume_data.get('years_experience', 0)
    
    if required_years > 0:
        if candidate_years >= required_years:
            score += exp_points
        else:
            # Partial points for experience
            score += (candidate_years / required_years) * exp_points
    else:
        # If no experience requirement, grant partial points
        score += exp_points * 0.5
    
    # Additional qualifications (20% of total score)
    cert_points = 20
    total_points += cert_points
    
    # Simple check for certifications
    if resume_data.get('certifications', []):
        score += cert_points
    
    # Calculate final percentage
    final_score = int(round((score / total_points) * 100))
    
    # Ensure score is in valid range
    return max(0, min(100, final_score))