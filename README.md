# Retrieval-Augmented-Generation-System

## Overview

The **Retrieval-Augmented-Generation-System (RAG)** is an advanced application combining retrieval-based question answering with generative capabilities powered by **Groq’s hardware acceleration**. The system uses **FastAPI** for the backend and integrates with **Groq’s API** for large language model (LLM) inference. It is containerized with **Docker**, orchestrated with **Kubernetes**, and deployed on **AWS Cloud** for scalability, high availability, and resilience.

## Features

- **FastAPI Backend**: High-performance, easy-to-use RESTful API.
- **Groq API Integration**: Uses **Groq's hardware and API** for accelerated large language model inference.
- **Dockerized**: Containerized for consistent deployment environments.
- **Kubernetes Orchestration**: Automatically scales and ensures high availability.
- **AWS Cloud Infrastructure**: Utilizes AWS cloud services for scalable hosting.
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval of relevant documents with generative text for better quality and accuracy in responses.

## Architecture

1. **FastAPI Backend**: Handles user queries, processes them using Groq's API for inference, and integrates a retrieval-based system for additional context.
2. **Groq API Integration**: Groq's API provides accelerated inference using their specialized hardware for large-scale models.
3. **Retrieval System**: Fetches relevant documents from a knowledge base or external data sources to improve the generative responses.
4. **Docker**: Ensures consistent deployment by packaging the app and all dependencies into containers.
5. **Kubernetes**: Orchestrates containers for scaling, fault tolerance, and easy management in production.
6. **AWS Cloud**: AWS provides cloud resources for hosting and scaling the application.

## Getting Started

### Prerequisites

To get started with this project, you will need:

- **Docker**: To containerize the application.
- **Kubernetes**: For scalable and resilient deployments.
- **AWS Account**: For deploying the application on AWS services like EC2, EKS, and S3.
- **Python 3.8+**: To run the FastAPI application locally or in Docker.
- **Groq API Key**: Required to interact with Groq's API for hardware-accelerated inference.

### Installation

1. **Clone the repository**:

    ```bash
    git clone hhttps://github.com/shravakushwaha/Retrieval-Augmented-Generation-system.git
    cd Retrieval-Augmented-Generation-system
    cd app
    ```

2. **Set up the Python environment** (optional if using Docker):

    ```bash
    python3 -m venv ragenv
    source ragenv/bin/activate  # On Windows, use 'ragenv\Scripts\activate'
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Groq API Key**:

    Set your **Groq API Key** as an environment variable:

    ```bash
    GROQ_API_KEY="your-groq-api-key"
    ```

    (On Windows, use `set` instead of `add`)

5. **Docker Setup**:

    Build and run the Docker container:

    ```bash
    docker build -t rag-system .
    docker run -d -p 8000:8000 rag-system
    ```

    The FastAPI application will be running at `http://localhost:8000`.

6. **Kubernetes Deployment**:

    Deploy the application to a Kubernetes cluster (e.g., AWS EKS, GKE, or your own Kubernetes cluster).

    Example deployment:

    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

7. **AWS Cloud Setup**:

    Set up the AWS environment (e.g., EC2, EKS) for hosting the application and manage IAM roles, security groups, and networking.

    Deploy the containerized application using AWS services.


## Running Tests with pytest

This project uses `pytest` for testing.

### **Installation**
Ensure you have pytest installed:
```bash
pip install pytest
```

## Running pytest Application Locally

This project uses `pytest` for testing.
```bash
pytest
```


### Running the Application Locally

To run the FastAPI application locally:

```bash
uvicorn main:app --reload
