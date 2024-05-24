from PIL import Image
import streamlit as st
from riskmitigationassist import risk_mitigation_assistant, save_api_key, open_ai_model
from prompt import prompt

# page config
st.set_page_config(
        page_title="Lyzr - Risk Mitigation Assistant",
        layout="centered",   
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

# style the app
st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)


# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Risk Mitigation Assistant')
st.markdown('A tool that uses AI to suggest customized risk mitigation strategies based on insurance types, offering tailored advice to reduce risks and enhance preparedness.')

# Setting up the sidebar for input
st.sidebar.title("Risk Mitigation Assistant")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type='password')
submit_api_key = st.sidebar.button("Submit API Key")

if api_key != "":
    if submit_api_key:
        save_api_key(api_key)
        st.sidebar.success("API Key saved!")


    with open('api_key.txt', 'r') as file:
        api_key = file.read()
        api_key = api_key.replace(" ","")

    open_ai = open_ai_model(API_KEY=api_key)

    agent = prompt.agent_prompt()
    policies = prompt.policies_types()


    insurace_type = st.selectbox(options=policies, label='Select your Insurance Type')


    if insurace_type != 'None':
        # if st.button('Submit'):
            policy_type = prompt.task_prompt(insurance_type=insurace_type)
            mitigation_starategies = risk_mitigation_assistant(insurance_type=policy_type, agent_prompt=agent, open_ai_model=open_ai, policy=insurace_type)
            st.markdown('---')
            st.subheader('Risk Mitigation Strategies')
            output = mitigation_starategies[0]['task_output']
            st.write(output)