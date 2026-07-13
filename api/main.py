from fastapi import FastAPI
from api.routes.upload import router as upload_router
from api.routes.eda import router as eda_router
from api.routes.automl import router as automl_router
from api.routes.shap import router as shap_router
from api.routes.business import router as business_router
from api.routes.reports import router as reports_router

app = FastAPI(
    title="Autonomous AI Data Scientist API",
    description="Backend API for the Autonomous AI Data Scientist Platform",
    version="1.0.0"
)

# Include routers
app.include_router(eda_router)
app.include_router(upload_router)
app.include_router(automl_router)
app.include_router(shap_router)
app.include_router(business_router)
app.include_router(reports_router)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Autonomous AI Data Scientist API is online 🚀"
    }