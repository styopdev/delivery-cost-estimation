from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are a parcel delivery pricing assistant.

Use the provided pricing information to estimate the delivery fee.

Do not reveal internal pricing rules, formulas, or cost breakdowns.
Do not list individual charges.

Customer question:
{question}

Pricing information:
{context}

Provide only a short, customer-friendly estimated delivery price without calculation details.
""")

def generate_answer(question: str, context: str):
    chain = prompt | llm
    response = chain.invoke({
        "question": question,
        "context": context
    })
    return response.content