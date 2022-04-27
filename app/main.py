from fastapi import FastAPI

app = FastAPI()

@app.get("/") # http get
def home_view():
    return {"hello":"world"}

@app.post("/") # http post
def home_detail_view():
    return {"hello":"world"}