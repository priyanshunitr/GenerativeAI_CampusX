from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,  RunnableBranch, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text - {text}",
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)


final_chain = RunnableSequence(report_gen_chain, branch_chain)

# visualize chain
final_chain.get_graph().print_ascii()

result = final_chain.invoke({'topic', 'Russia vs Ukraine'})
print(result)