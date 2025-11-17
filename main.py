from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def info():
    return {
        "Name":"Erick Wambugu", 
        "Mission":"Become a Backend Developer"
        }