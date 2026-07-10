# TDDS041B
from fastapi import fastAPI
app = FastAPI()
@app.get("/")
def home():
    return{ "message: wellcome to student CRUD api"}

