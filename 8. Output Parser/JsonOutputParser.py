from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = JsonOutputParser()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# prompt = template1.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template1 | model | parser
final_result = chain.invoke({})   # have to pass empty dictionary

print(final_result)
print(type(final_result))