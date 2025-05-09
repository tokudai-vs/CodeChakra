# Configuration settings for the AI code review agent

import os

class Config:
    # API settings
    API_KEY = os.getenv('API_KEY', 'your_default_api_key')
    API_URL = os.getenv('API_URL', 'http://localhost:5000/api')

    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')

    # Latency settings
    LATENCY_THRESHOLD = int(os.getenv('LATENCY_THRESHOLD', 200))  # in milliseconds

    # Risk analysis settings
    RISK_ANALYSIS_ENABLED = os.getenv('RISK_ANALYSIS_ENABLED', 'true').lower() == 'true'

    # Other settings can be added here as needed
