from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def add(x, y):
    return x + y

#var=
result = add(1, 2)
print("This is the sum: 1, 2, %s" % result)