from fastapi import FastAPI
from pydantic import BaseModel

from .agent import DsAgent

app = FastAPI(title="dsagent")
agent = DsAgent()

class QueryRequest(BaseModel):
    prompt: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/query")
def query(request: QueryRequest):
    response = agent.process(request.prompt)
    return {"prompt": request.prompt, "response": response}
