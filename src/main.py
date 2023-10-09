from routes import app
import os

HOST = os.getenv('HOST', "::")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host= HOST, port=4005)