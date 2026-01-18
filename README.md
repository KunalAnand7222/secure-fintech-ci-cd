# Secure Fintech CI/CD Pipeline

A production-ready **DevSecOps CI/CD pipeline** for a fintech-style backend application.  
This project automates **testing, Docker image builds, security scanning, and deployment** using modern DevOps best practices.

---

## 🚀 Overview

This repository demonstrates a secure and reliable CI/CD workflow suitable for fintech environments.  
Every push to the `main` branch triggers automated checks to ensure **code quality, container security, and deployment readiness**.

---

## 🧱 Architecture
Developer
   ↓
GitHub Repository
   ↓
GitHub Actions CI/CD
   ├── Run Unit Tests
   ├── Build Docker Image
   ├── Security Scan (Trivy)
   └── Deploy via Docker Compose

🛠 Tech Stack

Backend: FastAPI (Python)

CI/CD: GitHub Actions

Containers: Docker, Docker Compose

Security: Trivy (image vulnerability scanning)

Testing: Pytest

🔐 Security & DevSecOps

Automated vulnerability scanning with Trivy

Pipeline fails on HIGH/CRITICAL findings

No secrets hardcoded (uses environment variables / GitHub Secrets)

Non-root Docker container execution

📁 Repository Structure
secure-fintech-ci-cd/
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/workflows/
│   └── ci-cd.yml
└── README.md

🌐 API Endpoints
Endpoint	Description
/health	Health check
/stocks	Sample stock price data

Example response:

[
  { "symbol": "AAPL", "price": 189.3 },
  { "symbol": "GOOGL", "price": 141.7 }
]

▶️ Run Locally (Without Docker)
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000


Open:

http://localhost:8000/health

http://localhost:8000/stocks

🐳 Run with Docker
docker build -t fintech-api .
docker run -p 8000:8000 fintech-api

📦 Run with Docker Compose
docker compose up -d
