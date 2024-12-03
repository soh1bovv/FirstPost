from fastapi import FastAPI,Body
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
def lobby():
    return "hello"

@app.post('/post')
def post(data=Body()):
    name = data['name']
    return JSONResponse({'message':'Hi '+ name})