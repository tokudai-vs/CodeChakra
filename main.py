if __name__ == "__main__":
    import os
    import sys

    # Add the src directory to the Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

    from fastapi import FastAPI
    from agent.review import ReviewAgent
    from api.routes import setup_routes

    def create_app() -> FastAPI:
        app = FastAPI()
        setup_routes(app)
        return app

    app = create_app()
    import uvicorn

    uvicorn.run(app)