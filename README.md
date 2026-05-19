# dsagent

Python-based dsagent starter project with a basic web API and Docker support.

## Features

- FastAPI application for agent endpoints
- Basic `dsagent` package structure
- `Dockerfile` for container image building
- `docker-compose.yml` for easy local startup
- Test example using `pytest`

## Quick Start

1. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

2. Run locally

```bash
uvicorn dsagent.main:app --reload
```

3. Build Docker image

```bash
docker build -t dsagent .
```

4. Run with Docker Compose

```bash
docker compose up --build
```

## Files

- `dsagent/main.py`: FastAPI app entrypoint
- `dsagent/agent.py`: simple agent behavior
- `Dockerfile`: container build definition
- `docker-compose.yml`: service definition
- `requirements.txt`: Python dependencies
