from fastapi import FastAPI
from mangum import Mangum

from src.api.users import router as users_router

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


app.include_router(users_router, prefix="/users")
handler = Mangum(app)