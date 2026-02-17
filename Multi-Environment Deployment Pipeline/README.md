# 🚀 Multi-Environment CI/CD Pipeline

A production-ready CI/CD pipeline demonstrating automated testing, Docker containerization, and multi-environment deployments with a manual approval gate for production.

---

## 🏗️ Architecture

```
Developer Push
      │
      ▼
┌─────────────┐     push to dev      ┌─────────────────┐
│  dev branch │ ──────────────────►  │  DEV Environment │
└─────────────┘                      └─────────────────┘
      │
      │ Pull Request
      ▼
┌─────────────┐   auto on PR to main  ┌──────────────────────┐
│   PR/main   │ ──────────────────►   │ STAGING Environment  │
└─────────────┘                       └──────────────────────┘
      │
      │ Merge to main
      ▼
┌─────────────┐   manual approval    ┌──────────────────────────┐
│ main branch │ ──────────────────►  │ 🔐 Human Approval Gate   │
└─────────────┘                      └──────────────┬───────────┘
                                                     │ Approved
                                                     ▼
                                      ┌──────────────────────────┐
                                      │  PRODUCTION Environment  │
                                      └──────────────────────────┘
```

---

## 📁 Project Structure

```
CI-CD-pipelines/
├── app/
│   ├── app.py               # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── tests/
│       └── test_app.py      # Pytest test suite
├── .github/
│   └── workflows/
│       ├── dev.yml          # Auto-deploy to dev on push
│       ├── staging.yml      # Auto-deploy to staging on PR
│       └── production.yml   # Deploy to prod with approval gate
├── Dockerfile               # Container definition
├── docker-compose.yml       # Local multi-environment setup
├── .gitignore
└── README.md
```

---

## ⚙️ Pipeline Workflows

### 1. Development (`dev.yml`)
- **Trigger:** Push to `dev` branch
- **Steps:** Test → Build Docker image → Deploy to dev
- **Purpose:** Fast feedback loop for developers

### 2. Staging (`staging.yml`)
- **Trigger:** Pull Request to `main`
- **Steps:** Test → Build Docker image → Deploy to staging → Smoke tests → Comment on PR
- **Purpose:** Validate changes before production

### 3. Production (`production.yml`)
- **Trigger:** Push/merge to `main`
- **Steps:** Test → Build Docker image → **Manual Approval** → Deploy to production
- **Purpose:** Safe, controlled production deployments

---

## 🔐 Setting Up the Manual Approval Gate

1. Go to your GitHub repo → **Settings**
2. Click **Environments** → **New environment** → name it `production`
3. Enable **Required reviewers**
4. Add yourself (or your team) as a reviewer
5. Now every production deploy will pause and send you an email to approve ✅

---

## 🛠️ Prerequisites

- Docker & Docker Compose installed
- GitHub account
- Docker Hub account

---

## 🚀 Getting Started

### Run Locally

```bash
# Clone the repo
git clone https://github.com/greatnessawara/CI-CD-pipelines.git
cd CI-CD-pipelines

# Run all environments locally
docker-compose up

# Access the app
# Dev:        http://localhost:5000
# Staging:    http://localhost:5001
# Production: http://localhost:5002
```

### Run Tests Locally

```bash
pip install -r app/requirements.txt
pytest app/tests/ -v
```

---

## 🔑 GitHub Secrets Required

Go to **Settings → Secrets and variables → Actions** and add:

| Secret Name | Description |
|---|---|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password or access token |

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Home - returns app info and environment |
| `/health` | GET | Health check endpoint |
| `/version` | GET | Returns current version |

---

## 🧪 Test Coverage

- ✅ Home route returns 200 and correct payload
- ✅ Health endpoint returns healthy status
- ✅ Version endpoint returns version info

---

## 🔮 What's Next

- [ ] Add DevSecOps security scanning (Trivy, GitLeaks)
- [ ] Add Slack notifications on deploy
- [ ] Migrate to Kubernetes deployment
- [ ] Add GitOps with ArgoCD

---

## 👨‍💻 Author

**Greatness Awara** — DevOps & Cloud Engineer  
[LinkedIn](https://www.linkedin.com/in/awara-greatness-1a8b03276/) • [GitHub](https://github.com/greatnessawara)
