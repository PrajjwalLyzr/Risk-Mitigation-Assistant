def agent_prompt():
    prompt = """
            You are an intelligent assistant specialized in risk management and insurance advisory. Your task is to provide a detailed risk analysis and mitigation strategy based on a chosen type of insurance. 

    """

    return prompt


def task_prompt(insurance_type):
    prompt = f"""
                1. Risk Analysis: Based on the chosen insurance type: {insurance_type}, analyze potential risks associated with that specific coverage. Highlight common and significant risks that policyholders might face.

                2. Mitigation Strategy Generation: Based on the analyzed risks, generate a list of personalized risk mitigation strategies. These strategies should be practical, actionable, and tailored to the specific risks identified.
                
                3. Preparedness tips: Recommendations for being prepared in case risks materialize.
        """
    
    return prompt


def policies_types():
    types = [
        'None',
        "Health Insurance",
        "Life Insurance",
        "Auto Insurance",
        "Homeowners Insurance",
        "Renters Insurance",
        "Disability Insurance",
        "Long-term Care Insurance",
        "Travel Insurance",
        "Pet Insurance",
        "Business Insurance",
        "Workers' Compensation Insurance",
        "Liability Insurance",
        "Flood Insurance",
        "Earthquake Insurance",
        "Umbrella Insurance",
        "Title Insurance",
        "Dental Insurance",
        "Vision Insurance",
        "Boat Insurance",
        "Motorcycle Insurance",
        "RV Insurance",
        "Mobile Home Insurance",
        "Condo Insurance",
        "Farm Insurance",
        "Cyber Insurance",
        "Identity Theft Insurance",
        "Event Insurance",
        "Mortgage Insurance",
        "Critical Illness Insurance",
        "Accident Insurance"
        ]
    
    return types