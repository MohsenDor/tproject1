from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Tomato"}

@app.post("/add")
async def root(x:str=Body(...),y:int=Body(...)):
    return {x: y}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)