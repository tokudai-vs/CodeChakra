import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.main import create_app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(create_app())
