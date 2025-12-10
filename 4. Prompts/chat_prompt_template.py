from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate


# when to use - when we want to pass dynamic prompt with multiturn conversation

# this won't work
# chat_template = ChatPromptTemplate([
#     SystemMessage("You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])


chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({
    'domain': 'F1',
    'topic': "DRS"
})

print(prompt)