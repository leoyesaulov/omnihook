import subprocess
from http import HTTPStatus
import os
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

