def agent_prompt():
    prompt = """
            You are an intelligent assistant specialized in risk management and insurance advisory. Your task is to provide a detailed risk analysis and mitigation strategy based on a chosen type of insurance. 

    """

    return prompt


def task_prompt(insurance_details, Name):
    prompt = f"""

                Based on the following insurance policy details: '{insurance_details}', generate a list of personalized risk mitigation strategies:

                1. Risk Analysis:
                    - Based on insurance policy details: '{insurance_details}', analyze potential risks associated with that specific coverage. Highlight common and significant risks that policyholders might face.

                2. Mitigation Strategy Generation:
                    - Generate personalized 5 risk mitigation strategies on this policy deails: '{insurance_details}'. These strategies should be practical, actionable, and tailored to the specific risks identified.

                Provide a clear and concise list of actionable steps for {Name} to mitigate risks associated with their [Type of Insurance] policy. Please provide the information in a structured format

        """
    
    return prompt

def chat_prompt():
    prompt = """
                Extract the following information from the provided insurance policy document:

                1. Policy Holder Information:
                    - Name
                    - Address
                    - Contact Information

                2. Policy Details:
                    - Policy Number
                    - Type of Insurance (e.g., homeowners, auto, health)
                    - Effective Date
                    - Expiration Date

                3. Coverage Details:
                    - Coverage Limits
                    - Covered Events/Perils
                    - Exclusions
                    - Additional Coverage/Endorsements

                4. Deductibles:
                    - Deductible Amounts for Different Types of Claims

                5. Premium Information:
                    - Annual or Monthly Premium Amount
                    - Payment Schedule

                6. Claims History:
                    - Previous Claims Made
                    - Claim Amounts and Types

                7. Risk Mitigation Measures:
                    - Existing Safety and Security Measures

                Please provide the extracted information in a structured format.


            """
    
    return prompt
