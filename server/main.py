from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.auth import router as auth_router

app = FastAPI()

# Allow interactions from the frontend
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Chatbot Backend is Running"}
