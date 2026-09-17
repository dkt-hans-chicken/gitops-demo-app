# gitops-demo-app

Application source code. CI builds and pushes Docker image, then updates the manifest repo.

## Flow

```
git push → GitHub Actions
               ├── Build Docker image
               ├── Push to Docker Hub
               └── Update image tag in gitops-demo-manifests
                           ↓
                       ArgoCD detects change
                           ↓
                       Syncs to test-cluster/staging
```

## GitHub Secrets required

| Secret | Value |
|---|---|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `MANIFEST_REPO` | `your-org/gitops-demo-manifests` |
| `MANIFEST_REPO_TOKEN` | GitHub PAT with repo write access |

## Local dev

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload

# Visit http://localhost:8000
# Visit http://localhost:8000/health
```

## Docker build locally

```bash
cd app
docker build -t gitops-demo:local .
docker run -p 8000:8000 gitops-demo:local
```
# gitops-demo
