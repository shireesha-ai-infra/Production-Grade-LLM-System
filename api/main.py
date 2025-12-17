from fastapi import FastAPI
from inference.llm_client import generate

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.post("/query")
def query_llm(user_query:str):
    response = generate(user_query)
    return {"answer " : response}
