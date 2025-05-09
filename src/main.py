# filepath: /ai-code-review-agent/ai-code-review-agent/src/main.py

from fastapi import FastAPI
from agent.review import ReviewAgent
from api.routes import setup_routes

def create_app() -> FastAPI:
    app = FastAPI()
    setup_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)