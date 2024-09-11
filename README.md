# test_docker_cicd_py

**Author**: Haobo Yuan

This repository contains a Python application containerized with Docker and integrated with a full CI/CD pipeline. The project uses GitHub Actions for automatic building, linting, and testing of the Docker image before pushing it to Docker Hub. This is a test  used to learn how to setup an environment with Docker, GitHub, CI/CD, Python. This is a part of Duke Univ IDS-706(Fall 24') Homework 1: Create Python Template.

## Useful Links

- Docker Hub Repo
> https://hub.docker.com/r/haoboyuanduke/test_docker_cicd_py

- One of succeesful CI/CD run records
> https://github.com/haobo-yuan/test_docker_cicd_py/actions/runs/10795115655/job/29940998991

---

## Features
- Containerized Python application for consistency and portability
- Automated CI/CD pipeline using GitHub Actions
- Linting, testing, and building tasks defined in the workflow
- Docker image automatically pushed to Docker Hub upon successful tests

## Setup Instructions

### Prerequisites
- Docker installed on your machine
- Python 3.x installed locally
- A GitHub and Docker Hub account

### Steps to Set Up Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t your-username/your-repository:latest .
    ```

3. **Run the container**:
    ```bash
    docker run -it your-username/your-repository:latest
    ```

## Usage Instructions

Once the Docker container is running, you can interact with the Python application inside the container. For example, if your application includes a web server, you can access it through the exposed port.

### Running Tests
To run the tests, use the following Docker command:
```bash
docker run -it your-username/your-repository:latest pytest

## Reference

Simple python docker dev example for the official docker docs
> https://docs.docker.com/language/python/containerize/
> https://docs.docker.com/guides/language/python/configure-ci-cd/

Python Project Scaffold and Makefile Setup, from coursera by Prof. Gift
> https://www.coursera.org/videos/cloud-computing-foundations-duke/dxL50?query=scaffold&source=search
