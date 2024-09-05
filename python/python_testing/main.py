from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/repeat_text")
def repeat_text(text: str, times: int):
    if times >= 5:
        raise HTTPException(
            status_code=400, detail="The 'times' parameter must be less than 5."
        )
    return text * times
