import subprocess
from http import HTTPStatus
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

@app.post("/github/professional")
def professional():
    subprocess.run(['bash', 'professional.sh'])
    return HTTPStatus(200)

@app.post("/github/omnihook")
def omnihook():
    subprocess.run(['bash', ['omnihook.sh']])
    return HTTPStatus(200)

@app.post("/github/smartlife")
def smartlife():
    subprocess.run(['bash', ['smartlife.sh']])
    return HTTPStatus(200)