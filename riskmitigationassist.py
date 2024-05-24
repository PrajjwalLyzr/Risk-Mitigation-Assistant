from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger


def open_ai_model(API_KEY):
    open_ai_model_text = OpenAIModel(
        api_key= API_KEY,
        parameters={
            "model": "gpt-4-turbo-preview",
            "temperature": 0.5,
            "max_tokens": 1500,
        },
    )

    return open_ai_model_text


def risk_mitigation_assistant(insurance_type, agent_prompt, open_ai_model, policy):
    
    insurance_advisory = Agent(
        prompt_persona=agent_prompt,
        role="Risk Mitigation Assistant", 
    )

    mitigation_strategies =  Task(
        name="Personalized Risk Mitigation Assistant",
        agent=insurance_advisory,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model,
        instructions=f"{insurance_type} [!Important] Exclude the conclusion and summary",
        log_output=True,
        enhance_prompt=False,
        default_input=policy
    )


    logger = Logger()
    

    main_output = LinearSyncPipeline(
        logger=logger,
        name="Risk Mitigation Assistant",
        completion_message="App Generated all things!",
        tasks=[
            mitigation_strategies,   
        ],
    ).run()

    return main_output


def save_api_key(key):
    with open("api_key.txt", "w") as file:
        file.write(key)