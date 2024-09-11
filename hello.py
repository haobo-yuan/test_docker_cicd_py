# example from Docker docs
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# example from Prof. Gift
def add(x, y):
    return x + y


result = add(1, 2)
print("This is the sum: 1, 2, %s" % result)
