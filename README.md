# DevOps Portfolio - Kubernetes CI/CD Pipeline

A production-grade Kubernetes deployment pipeline demonstrating infrastructure automation, security best practices, and GitOps principles.

## Project Overview

This project implements a complete DevOps workflow for deploying a containerized application to Kubernetes with automated testing, security scanning, and continuous deployment. The environment runs in GitHub Codespaces with ArgoCD managing deployments to a local Kind cluster.

## Architecture
```
GitHub Push → CI Pipeline → Security Scan → Container Registry → ArgoCD → Kubernetes
```

### Components

- **Application**: FastAPI microservice with health checks and Prometheus metrics
- **Container Runtime**: Docker with multi-stage, security-hardened builds
- **Orchestration**: Kubernetes (Kind) with production-ready manifests
- **CI/CD**: GitHub Actions with automated testing and vulnerability scanning
- **GitOps**: ArgoCD for declarative, automated deployments
- **Security**: Trivy scanning, non-root containers, network policies, pod security standards

## Quick Start

### Prerequisites

- GitHub account with Codespaces access
- 2GB+ Codespace (included in free tier)

### Launch the Environment

1. Fork this repository
2. Open in GitHub Codespaces (Code → Codespaces → Create codespace on main)
3. Wait for devcontainer to build (approximately 3 minutes)
4. Cluster and ArgoCD are automatically configured

### Verify Deployment
```bash
# Check cluster status
kubectl get nodes

# View ArgoCD application
kubectl get application -n argocd

# Check running pods
kubectl get pods -n portfolio-app

# Test the application
kubectl port-forward -n portfolio-app svc/fastapi-service 8000:80
curl http://localhost:8000/health
```

## Features

### Infrastructure as Code
- Kubernetes manifests with Kustomize overlays
- Declarative application deployment via ArgoCD
- Reproducible development environment using devcontainers

### CI/CD Pipeline
- Automated testing with pytest on every pull request
- Dockerfile linting with Hadolint
- Kubernetes manifest validation with kubeval
- Trivy vulnerability scanning with results uploaded to GitHub Security
- Automatic container builds pushed to GitHub Container Registry
- Git SHA-based image tagging for traceability

### Security Implementation
- Multi-stage Docker builds minimizing attack surface
- Non-root containers (UID 1000)
- Read-only root filesystem
- All Linux capabilities dropped
- Kubernetes network policies enforcing zero-trust networking
- Pod security standards
- Resource limits preventing resource exhaustion
- Automated vulnerability scanning in CI/CD pipeline

Detailed security analysis available in [docs/security.md](docs/security.md).

### Scalability and Reliability
- Horizontal Pod Autoscaler for CPU-based scaling
- Liveness and readiness probes
- Resource requests and limits defined
- Multiple replicas for high availability

### Observability
- Prometheus metrics endpoint at `/metrics`
- Structured application logging
- Health check endpoints for monitoring
- ArgoCD deployment status tracking

## Project Structure
```
.
├── .devcontainer/          # Codespaces environment configuration
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline definition
├── app/
│   ├── app.py              # FastAPI application
│   ├── Dockerfile          # Multi-stage container build
│   ├── requirements.txt    # Python dependencies
│   └── tests/              # pytest test suite
├── k8s/
│   ├── base/               # Base Kubernetes manifests
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── ingress.yaml
│   │   ├── hpa.yaml
│   │   └── network-policy.yaml
│   └── argocd-app.yaml     # ArgoCD application definition
└── docs/
    └── security.md         # Security analysis and posture
```

## CI/CD Workflow

### Pull Request Pipeline
1. Execute unit tests using pytest
2. Lint Dockerfile with Hadolint and Kubernetes manifests with kubeval
3. Build container image
4. Run Trivy vulnerability scan
5. Upload security findings to GitHub Security tab
6. Block merge on CRITICAL or HIGH severity vulnerabilities

### Main Branch Pipeline
1. Complete all pull request checks
2. Build and tag container image with git SHA
3. Push to GitHub Container Registry
4. ArgoCD detects manifest changes
5. Automatically syncs deployment to Kubernetes cluster
6. Rolling update ensures zero-downtime deployment

## Security Posture

Current vulnerability scan results:
- Python application dependencies: 0 vulnerabilities
- Base OS packages: 109 vulnerabilities (primarily OpenSSL and glibc in Debian base image)
  - 3 CRITICAL, 9 HIGH, 46 MEDIUM, 51 LOW
  - Mitigated through container hardening, network isolation, and runtime security controls
  
Complete security analysis available in [docs/security.md](docs/security.md).

## Technology Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.11 |
| Framework | FastAPI |
| Container Runtime | Docker |
| Orchestration | Kubernetes (Kind) |
| CI/CD | GitHub Actions |
| GitOps | ArgoCD |
| Security Scanning | Trivy |
| Metrics | Prometheus |
| Development Environment | GitHub Codespaces |

## Performance Metrics

- CI pipeline execution: approximately 2 minutes
- ArgoCD sync time: less than 30 seconds
- Container image size: approximately 150MB (multi-stage build optimization)
- Test coverage: 100% of critical endpoints

## Skills Demonstrated

- Container orchestration with Kubernetes (deployments, services, ingress, horizontal pod autoscaling)
- CI/CD pipeline design and implementation using GitHub Actions
- GitOps practices with ArgoCD
- Security hardening (vulnerability scanning, container security, network policies, least privilege)
- Infrastructure as Code using Kubernetes manifests and Kustomize
- Observability implementation (health checks, metrics, logging)
- DevOps best practices (trunk-based development, semantic versioning, comprehensive documentation)

## Potential Enhancements

- Multi-environment deployment strategy (development, staging, production)
- Helm chart implementation for manifest templating
- Custom metrics-based horizontal pod autoscaling
- Service mesh integration (Istio or Linkerd)
- Distributed tracing with Jaeger or Tempo
- External secrets management (Sealed Secrets or External Secrets Operator)
- Backup and disaster recovery with Velero
- Cost optimization analysis using Kubecost

## License

MIT License

## Contact

**Tim Brown**  
GitHub: [fc2brown](https://github.com/fc2brown)  
LinkedIn: [https://www.linkedin.com/in/tbgolden](#)  
Email: fc2brown@gmail.com

---

*This portfolio demonstrates senior-level DevOps and Infrastructure Engineering capabilities.*
