from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import gradio as gr

# Load the model and tokenizer from HuggingFace
model_name = "gpt2"  # You can try "tiiuae/falcon-rw-1b" or "Salesforce/codegen-350M-mono"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create the pipeline
text_gen = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
hf_llm = HuggingFacePipeline(pipeline=text_gen)

# Prompt template with few-shot example and chain-of-thought prompting
prompt_template = PromptTemplate.from_template(
    '''You are an assistant that generates Python docstrings for given functions.
Here is an example:

Function:
def add(a, b):
    return a + b

Docstring:
\"\"\"Adds two numbers and returns the sum.\"\"\"

Now generate a docstring for the following function:

Function:
{function_code}

Docstring:
\"\"\"'''
)

# Create the LangChain LLM chain
docstring_chain = LLMChain(llm=hf_llm, prompt=prompt_template)

# Function to call the chain and return the result
def generate_docstring(code):
    try:
        result = docstring_chain.run({"function_code": code})
        return result.strip() + '\"\"\"'  # Close the docstring
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
iface = gr.Interface(
    fn=generate_docstring,
    inputs=gr.Textbox(lines=10, label="Enter Python Function Code"),
    outputs=gr.Textbox(lines=5, label="Generated Docstring"),
    title="AI Python Docstring Generator",
    description="Paste a Python function and get an auto-generated docstring using an LLM."
)

if __name__ == "__main__":
    iface.launch()

