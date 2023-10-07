from fastapi import FastAPI
from routes import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="::", port=4005)