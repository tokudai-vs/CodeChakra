from fastapi import FastAPI
from .api.routes import setup_routes


def create_app() -> FastAPI:
    app = FastAPI()
    setup_routes(app)
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
