# GitHub Gists API

A FastAPI application that fetches GitHub Gists for a given user.
The reason for choosing FastAPI web framework was due to its high performance and it provides Swagger out of the box for testing API endpoint.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

## Local Setup

### 1. Clone the repository and navigate to project folder
```bash
git clone <repository-url>
cd github_gist
```

### 2. Create a virtual environment
from the github_gist directory, execute below:
```bash
python -m venv myenv
```

### 3. Activate the virtual environment

**On Windows (PowerShell):**

myenv\Scripts\Activate.ps1

**On Windows (Command Prompt):**
myenv/Scripts/activate.bat

### 4. Install dependencies

pip install -r requirements.txt

## Running the Application

### Using Uvicorn (Development)
uvicorn main:app --reload --port 8080

The API will be available at `http://localhost:8080`

### API Endpoint
```
GET /{username}
```
Fetches all gists for the given GitHub username.

**Example:**
http://localhost:8080/octocat

**Output Format**
The output will be list of gists, with each element in gists in format as below : 
[{
    "id": "",
    "description": "",
    "url": "",
    "files": [
      "",""
    ]
}]

## Swagger Availability
Swagger UI will be available at URL : http://localhost:8080/docs#/

## Running application through Docker :
# Build the Docker image
docker build -t myapp .

# Run the container (maps port 8080 from container to host)
docker run -p 8080:8080 myapp

In this case as well, application will be available at http://localhost:8080/
Eg : http://localhost:8080/octocat

## Running Tests

### Run pytest
```bash
pytest -v
```

This will run all tests in the `tests/` directory with verbose output.



## Project Structure

```
github_gist/
├── services/
│      └── github_api.py      # GitHub API integration
├── tests/
│   ├── __init__.py            # Tests package marker
│   └── test_api.py            # API tests
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── pytest.ini                 # Pytest configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Dependencies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **httpx** - Async HTTP client
- **pytest** - Testing framework
- **pytest-asyncio** - Async test support

## Troubleshooting

### Module not found errors
Make sure your virtual environment is activated and all dependencies are installed.

### Port 8080 already in use
Run on a different port:
```bash
uvicorn main:app --reload --port 8001
```