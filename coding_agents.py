import langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.prompts import PromptTemplate
# Define a simple tool for demonstration
def greet(name: str) -> str:
    return f"Hello, {name}!"


greet_tool = Tool(
    name="greet",
    func=greet,
    description="Greets a person with their name."
)
# Initialize the language model
llm = ChatOpenAI(temperature=0)
# Define a custom prompt template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="You are a helpful assistant. {input}"
)
# Initialize the agent with the tool and custom prompt
agent = initialize_agent(
    tools=[greet_tool],
    llm=llm,        
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    prompt=prompt_template
)
# Example usage of the agent
if __name__ == "__main__":
    user_input = "Please greet John."
    response = agent.run(user_input)
    print(response)
    
