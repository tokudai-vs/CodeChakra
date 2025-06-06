# AI Code Review Agent

## Overview
The AI Code Review Agent is designed to assist development teams in reviewing pull requests (PRs) by identifying potential performance bottlenecks, security issues, and logical errors. This agent leverages advanced AI techniques to provide insights and recommendations, making the code review process more efficient and effective.

## Features
- **Latency-Aware Reviews**: Simulates and analyzes performance to flag potential latency issues in PRs.
- **Risk Analysis**: Evaluates code for potential risks and bottlenecks, providing actionable insights.
- **Lightweight and Portable**: Built using FastAPI and Hugging Face, making it easy to deploy and extend.
- **Explainable Suggestions**: Offers explanations for suggested fixes, enhancing understanding and learning.
- **Analytics Component**: Logs and tracks latency metrics per PR, providing valuable data for development leads.

## Project Structure
```
ai-code-review-agent
├── src
│   ├── main.py                # Entry point for the application
│   ├── agent                   # Contains the review agent logic
│   │   ├── __init__.py
│   │   ├── review.py           # ReviewAgent class for PR analysis
│   │   └── risk_analysis.py     # RiskAnalyzer class for risk evaluation
│   ├── api                     # API routes for the application
│   │   ├── __init__.py
│   │   └── routes.py           # Defines API endpoints
│   ├── utils                   # Utility functions
│   │   ├── __init__.py
│   │   └── latency.py          # Functions to measure latency
│   ├── models                  # Data models for the application
│   │   ├── __init__.py
│   │   └── pr_review.py        # PRReview class for PR objects
│   └── config.py               # Configuration settings
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── tests                       # Unit tests for the application
    ├── __init__.py
    ├── test_review.py          # Tests for review functionality
    └── test_latency.py         # Tests for latency measurement
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/tokudai-vs/codechakra.git
   ```
2. Navigate to the project directory:
   ```
   cd codechakra
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the AI Code Review Agent, run the following command:
```
python src/main.py
```
This will initialize the agent and start the API server, allowing you to submit PRs for review.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.