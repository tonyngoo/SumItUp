from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain.docstore.document import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from operator import itemgetter
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Mounts the `static` folder within the `build` folder to the `/static` route.
app.mount('/static', StaticFiles(directory="./build/static"), 'static')

def AISummary(text):
    try:
        # Define our LLM
        llm = ChatOllama(model="llama3")

        summarize_system = """ You are a helpful assistant that is only used to summarize text. You will receive a text and must return a summary. 
        Try to be concise while still highlighting key details that you believe to be relevant.
        Avoid saying anything that is not relevant to the summary.
        If the text passage provided is not long enough or does not contain enough information to generate a summary, state that you cannot generate a summary with the given passage.
        """
        summarize_template = """Given the text passage below, provide a summary of it.
        If the text passage provided is not long enough or does not contain enough information to generate a summary, state that you cannot generate a summary with the given passage.
        Avoid saying anything that is not relevant to the summary, such as "Here is a summary".
        Be concise and direct.
        Text Passage: {text_passage}
        """

        summarize_prompt = ChatPromptTemplate.from_messages([("system", summarize_system), ("human", summarize_template)])

        # Load our documents
        splitter = CharacterTextSplitter()
        texts = splitter.split_text(text)
        docs = [Document(page_content=text) for text in texts]

        # Load a summarization chain with custom system and prompt
        chain = ({"text_passage": itemgetter("text_passage")}
                 | summarize_prompt
                 | llm
            | StrOutputParser()
        )

        # Invoke to run the chain and gather the results of the summarization
        result = chain.invoke({"text_passage": docs})

        return result

    except Exception as e:
        raise RuntimeError(f"Error generating summary: {e}")

# Pydantic structure to hold the incoming text from the endpoint
class TextRequest(BaseModel):
    text: str

# Endpoint that takes in text and responds with an AI generated summary of the text
@app.post("https://sumitup.onrender.com/summarize-text")
def create_section_summary(req: TextRequest):
    try:
        # Uses the LLM to create a generate a summary with the provided text
        text = req.text
        summary = AISummary(text)

        # Returns the summary
        return JSONResponse(content={"content": text, "summary": summary})
    
    # Catches any errors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing text: {str(e)}")
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=10000)