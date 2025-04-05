import re

def parse_resume(resume_data):
    """
    Process resume data to extract structured information
    
    Args:
        resume_data (dict): Raw resume information
        
    Returns:
        dict: Enriched resume data with extracted experience details
    """
    # Create a copy to avoid modifying the original
    parsed = resume_data.copy()
    
    # Extract years of experience
    years_exp = 0
    if 'experience' in resume_data and resume_data['experience']:
        # Look for patterns like (2019-2023) or (2019-present)
        exp_pattern = r'\((\d{4})[-–](\d{4}|present|current)\)'
        matches = re.findall(exp_pattern, resume_data['experience'], re.IGNORECASE)
        
        for match in matches:
            start_year = int(match[0])
            if match[1].lower() in ['present', 'current']:
                from datetime import datetime
                end_year = datetime.now().year
            else:
                end_year = int(match[1])
            
            years_exp += (end_year - start_year)
    
    # Normalize skills to uppercase for technologies and acronyms
    normalized_skills = []
    for skill in resume_data.get('skills', []):
        if skill.lower() in ['aws', 'sql', 'ui', 'ux', 'api', 'ci', 'cd']:
            normalized_skills.append(skill.upper())
        else:
            normalized_skills.append(skill)
    
    # Add the extracted information
    parsed['years_experience'] = years_exp
    parsed['skills'] = normalized_skills
    
    return parsed