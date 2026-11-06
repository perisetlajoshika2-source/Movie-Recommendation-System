from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

movies = pd.read_csv("dataset/movies.csv")

class MovieRequest(BaseModel):
    title: str

@app.post("/recommend")
def recommend(data: MovieRequest):

    recommendations = movies["Movie"].sample(5).tolist()

    return {
        "recommendations": recommendations
    }