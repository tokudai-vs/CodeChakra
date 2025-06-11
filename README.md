# AI Code Review Agent

## Overview
The AI Code Review Agent is designed to assist development teams in reviewing pull requests (PRs) by identifying potential performance bottlenecks, security issues, and logical errors. This agent leverages advanced AI techniques to provide insights and recommendations, making the code review process more efficient and effective.

This project now leverages **LangGraph** to coordinate multiple specialized agents.
│   │   ├── language_detector.py  # Detects programming language
│   │   ├── static_analyzer.py   # Static code analysis
## Features
- **Latency-Aware Reviews**: Simulates and analyzes performance to flag potential latency issues in PRs.
- **Risk Analysis**: Evaluates code for potential risks and bottlenecks, providing actionable insights.
- **Lightweight and Portable**: Built using FastAPI and Hugging Face, making it easy to deploy and extend.
- **Explainable Suggestions**: Offers explanations for suggested fixes, enhancing understanding and learning.
- **Analytics Component**: Logs and tracks latency metrics per PR, providing valuable data for development leads.
- **Language Detection**: Identifies the programming language of code snippets before analysis.
- **Static Code Analysis**: Reports basic complexity metrics using lizard.
- **Agentic Workflow**: Orchestrated using LangGraph for modular analysis.

## Project Structure
```
ai-code-review-agent
├── src
│   ├── main.py                # Entry point for the application
│   ├── agent                   # Contains the review agent logic
│   │   ├── __init__.py
│   │   ├── review.py           # ReviewAgent class for PR analysis
│   │   ├── language_detector.py  # Detects programming language
│   │   ├── static_analyzer.py   # Static code analysis
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
    ├── test_language_detector.py # Tests for language detection
    └── test_static_analyzer.py   # Tests for static analysis
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
## Webhook Integration
Configure GitHub or Bitbucket to call the API whenever a pull request is created.

- **GitHub**: send 'pull_request' events to '/webhook/github'.
- **Bitbucket**: send 'pullrequest:created' events to '/webhook/bitbucket'.

Set 'GITHUB_TOKEN' and 'BITBUCKET_TOKEN' environment variables so the server can fetch PR diffs.


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
