# dsagent

Python-based dsagent starter project with a basic web API and Docker support.

基于 Python 的 dsagent 启动项目，包含基础 Web API 和 Docker 支持。

## Features / 功能

- FastAPI application for agent endpoints
- FastAPI 应用，用于 agent 接口
- Basic `dsagent` package structure
- 基础 `dsagent` 包结构
- `Dockerfile` for container image building
- `Dockerfile` 用于构建容器镜像
- `docker-compose.yml` for easy local startup
- `docker-compose.yml` 用于本地快速启动
- Test example using `pytest`
- 使用 `pytest` 的测试示例

## Quick Start / 快速开始

1. Install dependencies / 安装依赖

```bash
python3 -m pip install -r requirements.txt
```

2. Run locally / 本地运行

```bash
uvicorn dsagent.main:app --reload
```

3. Build Docker image / 构建 Docker 镜像

```bash
docker build -t dsagent .
```

4. Run with Docker Compose / 使用 Docker Compose 运行

```bash
docker compose up --build
```

## Files / 文件说明

- `dsagent/main.py`: FastAPI app entrypoint / FastAPI 应用入口
- `dsagent/agent.py`: simple agent behavior / 简单 agent 行为逻辑
- `Dockerfile`: container build definition / 容器构建定义
- `docker-compose.yml`: service definition / 服务定义
- `requirements.txt`: Python dependencies / Python 依赖
