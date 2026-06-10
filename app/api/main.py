from fastapi import FastAPI
from app.graph.workflow import graph

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Development Team Running"
    }


@app.post("/generate")
def generate_project(data: dict):

    result = graph.invoke(
        {
            "requirement": data["requirement"]
        }
    )

    return {
        "result": result
    }