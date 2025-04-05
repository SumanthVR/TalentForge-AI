def schedule_interview(candidate_name, email, match_score):
    """
    Generate email content for interview scheduling based on match score
    
    Args:
        candidate_name (str): Name of the candidate
        email (str): Email address of candidate
        match_score (int): Match percentage from matching algorithm
        
    Returns:
        str: Email content template
    """
    # Base email template
    email_subject = "Your Application - Next Steps"
    
    # Customize email content based on match score
    if match_score >= 80:
        email_content = f"""Subject: {email_subject}
        
Dear {candidate_name},

Thank you for your application. We're excited to share that your profile is a strong match for the position!

We'd like to invite you to an interview with our hiring team. Please use the link below to select a time that works for you:
[INTERVIEW SCHEDULING LINK]

Looking forward to meeting you soon!

Best regards,
TalentForge AI Recruiting Team"""

    elif match_score >= 60:
        email_content = f"""Subject: {email_subject}
        
Dear {candidate_name},

Thank you for your application. After reviewing your profile, we'd like to learn more about your experience and skills.

Please complete a brief skills assessment using the link below:
[SKILLS ASSESSMENT LINK]

We'll be in touch shortly after reviewing your results.

Best regards,
TalentForge AI Recruiting Team"""

    else:
        email_content = f"""Subject: {email_subject}
        
Dear {candidate_name},

Thank you for your interest in our position. After careful review, we've decided to pursue other candidates whose experience more closely aligns with our current needs.

We'll keep your resume in our database for future opportunities that may be a better match.

Best regards,
TalentForge AI Recruiting Team"""
    
    return email_content