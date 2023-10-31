from fastapi import FastAPI

app = FastAPI()

@app.get("/square/")
async def get_square(number: dict) -> dict:
    
    assert isinstance(number, dict), "Number should be a dictionary with key named value, Fix this issue!"
    assert "value" in number.keys(), "Incorrect key value pair given. Check the key name."
    assert isinstance(number["value"], float), "The value inside should be a float."
    
    number = number["value"]
    result = number * number
    
    print("This check happens.")
    
    return {
        "input": number,
        "result": result,
    }
    
@app.get("/")
async def say_hello() -> dict:
    return {
        "greeting": "hello, user!!"
    }