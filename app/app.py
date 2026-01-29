from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="DevOps Portfolio API", version="1.0.0")

# Prometheus metrics
request_counter = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

@app.get("/")
async def root():
    request_counter.labels(method='GET', endpoint='/').inc()
    logger.info("Root endpoint called")
    return {"message": "DevOps Portfolio API", "status": "running"}

@app.get("/health")
async def health():
    """Liveness probe endpoint"""
    return {"status": "healthy"}

@app.get("/ready")
async def ready():
    """Readiness probe endpoint"""
    return {"status": "ready"}

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

