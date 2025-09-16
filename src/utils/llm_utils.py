import base64
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
#from src.prompts import summarize_prompt
from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv())
_ = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.environ['GROQ_API_KEY']

# --- Image Description ---
def describe_image(image_path, image_ext):
    """Generate scientific description of an image using Groq Vision LLM."""
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    mime_type = f"image/{image_ext}" if image_ext != "jpg" else "image/jpeg"
    llm_vision = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct"
                          #model="llama-3.3-70b-versatile"
                          )

    prompt =   (
        "You are a real-life researcher analyzing a figure from a research paper. "
        "Describe this image in detail, summarizing its key elements, data, trends, "
        "and implications as you would in a research summary."
    )

    message = HumanMessage(content=[
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}}
    ])

    response = llm_vision.invoke([message])
    return response.content

# --- Text Summaries ---
def explain_document(text, question):
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    prompt_template = ChatPromptTemplate.from_template(
        "You are a real-life researcher. Based on the following context from a research paper, "
        "please answer this question: {question}\n\n--- Text Context ---\n{context}"
    )
    chain = prompt_template | llm
    return "".join(chunk.content for chunk in chain.stream({"question": question, "context": text[:8000]}))

def answer_followup(text, question):
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    prompt_template = ChatPromptTemplate.from_template(
        "You are a real-life researcher. Based on the following context from a research paper, "
        "please provide a detailed answer to this question: {question}\n\n--- Text Context ---\n{context}"
    )
    chain = prompt_template | llm
    return "".join(chunk.content for chunk in chain.stream({"question": question, "context": text[:8000]}))
