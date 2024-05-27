from PIL import Image
import streamlit as st
from riskmitigationassist import risk_mitigation_assistant, save_api_key, chatagent
from prompt import prompt
import os
from utils import utils

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

data = 'Data'
os.makedirs(data, exist_ok=True)


# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Risk Mitigation Assistant')
st.markdown('A tool that uses AI to suggest customized risk mitigation strategies based on insurance types, offering tailored advice to reduce risks and enhance preparedness.')

# Setting up the sidebar for input
st.sidebar.title("Risk Mitigation Assistant")
api_key = st.sidebar.text_input("First Enter your OpenAI API key", type='password')
submit_api_key = st.sidebar.button("Submit API Key")

if api_key != "":
    if submit_api_key:
        save_api_key(api_key)
        st.sidebar.success("API Key saved!")


col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input('User Name')

with col2:
    insurance_type = st.text_input('Your Insurance Type')

policy_doc = st.file_uploader(label='Upload your policy', type=['pdf','docx'])




if policy_doc is not None:
    utils.save_uploaded_file(directory=data, uploaded_file=policy_doc)
    current_directory = os.getcwd()
    files_in_directory = os.listdir(current_directory)
    if 'api_key.txt' in files_in_directory:
        with open('api_key.txt', 'r') as file:
            api_key = file.read()
            api_key = api_key.replace(" ","")
            os.environ['OPENAI_API_KEY'] = api_key
        
        if (user_name and insurance_type) != "":
            if st.button('Generate'):
                file = utils.get_files_in_directory(directory=data)
                prompt_ = prompt.chat_prompt()
                policy_info_ = chatagent(file,prompt=prompt_)
                agent_prompt_ = prompt.agent_prompt()
                mitigation_prompt_ = prompt.task_prompt(insurance_details=policy_info_, Name=user_name)
                mitigation_strategies_output = risk_mitigation_assistant(insurance_details=mitigation_prompt_, 
                                                                agent_prompt=agent_prompt_,
                                                                API_KEY=api_key,
                                                                policy=insurance_type)
                
                st.markdown('---')
                output = mitigation_strategies_output[0]['task_output']
                st.write(output)
                
        else:
            st.warning('Please Provide the necessary deatils such as Name and Insurance Type')

    else:
        st.warning('Please Submit your OpenAI API Key')

else:
    utils.remove_existing_files(directory=data)
    st.warning('Upload your policy document with necessary details')