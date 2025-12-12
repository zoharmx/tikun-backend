"""
Tikun Framework - Backend API Server
====================================
FastAPI server para ejecutar Tikun Framework desde frontend.

Endpoints:
- POST /api/analyze - Ejecutar análisis completo
- GET /api/status/{job_id} - Check status de análisis
- GET /api/results/{job_id} - Obtener resultados

Autor: Framework Tikun V2
Fecha: 2025-12-12
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
import asyncio
import json
from datetime import datetime
from pathlib import Path
import sys
import os

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Import Tikun Framework
from tikun_orchestrator import TikunOrchestrator

# Initialize FastAPI
app = FastAPI(
    title="Tikun Framework API",
    description="API para análisis ético con 10 Sefirot",
    version="2.0"
)

# CORS - Permitir frontend acceder a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev
        "http://localhost:5173",  # Vite dev
        "https://tikunframework.web.app",  # Production - Firebase
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for jobs (usar Redis/DB en producción)
jobs: Dict[str, Dict[str, Any]] = {}


# ============================================================================
# MODELS
# ============================================================================

class AnalysisRequest(BaseModel):
    """Request para análisis Tikun"""
    scenario: str
    case_name: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "scenario": "PROPUESTA: Implementar desalinización solar...",
                "case_name": "Desalination_Demo"
            }
        }


class AnalysisResponse(BaseModel):
    """Response con job_id para polling"""
    job_id: str
    status: str
    message: str
    estimated_time_seconds: int


class StatusResponse(BaseModel):
    """Status de análisis en progreso"""
    job_id: str
    status: str  # "pending", "running", "completed", "failed"
    progress: int  # 0-100
    current_sefira: Optional[str] = None
    elapsed_time_seconds: Optional[int] = None
    estimated_remaining_seconds: Optional[int] = None


class ResultsResponse(BaseModel):
    """Resultados completos del análisis"""
    job_id: str
    case_name: str
    status: str
    timestamp: str
    execution_time_seconds: float
    sefirot_results: Dict[str, Any]
    summary: Dict[str, Any]


# ============================================================================
# BACKGROUND TASK - EJECUTAR TIKUN
# ============================================================================

async def run_tikun_analysis(job_id: str, scenario: str, case_name: str):
    """
    Ejecuta Tikun Framework en background.
    Actualiza job status conforme progresa.
    """
    try:
        # Update status: running
        jobs[job_id]["status"] = "running"
        jobs[job_id]["started_at"] = datetime.now()
        
        # Initialize orchestrator
        orchestrator = TikunOrchestrator(verbose=False)
        
        # Progress callback
        def update_progress(sefira: str, progress: int):
            jobs[job_id]["current_sefira"] = sefira
            jobs[job_id]["progress"] = progress
        
        # Run analysis (blocking - en producción usar thread pool)
        results = orchestrator.process(scenario, case_name)
        
        # Store results
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["completed_at"] = datetime.now()
        jobs[job_id]["results"] = results
        jobs[job_id]["progress"] = 100
        
        # Calculate execution time
        elapsed = (jobs[job_id]["completed_at"] - jobs[job_id]["started_at"]).total_seconds()
        jobs[job_id]["execution_time_seconds"] = elapsed
        
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)
        jobs[job_id]["completed_at"] = datetime.now()


# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Health check"""
    return {
        "service": "Tikun Framework API",
        "version": "2.0",
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    }


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest, background_tasks: BackgroundTasks):
    """
    Inicia análisis Tikun en background.
    Retorna job_id para polling.
    
    Usage:
    ```javascript
    const response = await fetch('http://localhost:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            scenario: "PROPUESTA: ...",
            case_name: "Demo_Case"
        })
    });
    const { job_id } = await response.json();
    ```
    """
    # Validate scenario
    if not request.scenario or len(request.scenario) < 50:
        raise HTTPException(
            status_code=400, 
            detail="Scenario must be at least 50 characters"
        )
    
    # Generate job_id
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    case_name = request.case_name or f"Analysis_{timestamp}"
    job_id = f"{case_name}_{timestamp}"
    
    # Initialize job
    jobs[job_id] = {
        "job_id": job_id,
        "case_name": case_name,
        "scenario": request.scenario,
        "status": "pending",
        "progress": 0,
        "created_at": datetime.now(),
        "current_sefira": None
    }
    
    # Run analysis in background
    background_tasks.add_task(
        run_tikun_analysis,
        job_id,
        request.scenario,
        case_name
    )
    
    return AnalysisResponse(
        job_id=job_id,
        status="pending",
        message="Analysis started. Use job_id to check status.",
        estimated_time_seconds=180  # ~3 minutes
    )


@app.get("/api/status/{job_id}", response_model=StatusResponse)
async def get_status(job_id: str):
    """
    Check status de análisis.
    Poll cada 2-3 segundos desde frontend.
    
    Usage:
    ```javascript
    const checkStatus = async (jobId) => {
        const response = await fetch(`http://localhost:8000/api/status/${jobId}`);
        const status = await response.json();
        
        if (status.status === "completed") {
            // Fetch results
        } else if (status.status === "failed") {
            // Show error
        } else {
            // Update progress bar
            setTimeout(() => checkStatus(jobId), 2000);
        }
    };
    ```
    """
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs[job_id]
    
    # Calculate elapsed time
    elapsed = None
    estimated_remaining = None
    
    if "started_at" in job:
        elapsed = int((datetime.now() - job["started_at"]).total_seconds())
        
        # Estimate remaining (rough: 180s total)
        if job["progress"] > 0:
            total_estimated = elapsed / (job["progress"] / 100)
            estimated_remaining = int(total_estimated - elapsed)
    
    return StatusResponse(
        job_id=job_id,
        status=job["status"],
        progress=job["progress"],
        current_sefira=job.get("current_sefira"),
        elapsed_time_seconds=elapsed,
        estimated_remaining_seconds=estimated_remaining
    )


@app.get("/api/results/{job_id}", response_model=ResultsResponse)
async def get_results(job_id: str):
    """
    Obtiene resultados completos cuando status = "completed".
    
    Usage:
    ```javascript
    const response = await fetch(`http://localhost:8000/api/results/${jobId}`);
    const results = await response.json();
    
    console.log(results.sefirot_results.keter);
    console.log(results.sefirot_results.yesod.go_no_go_recommendation);
    ```
    """
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs[job_id]
    
    if job["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail=f"Analysis not completed. Current status: {job['status']}"
        )
    
    # Extract summary
    results = job["results"]
    sefirot = results["sefirot_results"]
    
    summary = {
        "keter_alignment": sefirot.get("keter", {}).get("alignment_percentage", 0),
        "keter_valid": sefirot.get("keter", {}).get("manifestation_valid", False),
        "yesod_recommendation": sefirot.get("yesod", {}).get(
            "go_no_go_recommendation", {}
        ).get("decision", "UNKNOWN"),
        "yesod_confidence": sefirot.get("yesod", {}).get(
            "go_no_go_recommendation", {}
        ).get("confidence", "unknown"),
        "execution_time": job.get("execution_time_seconds", 0)
    }
    
    return ResultsResponse(
        job_id=job_id,
        case_name=job["case_name"],
        status=job["status"],
        timestamp=job["completed_at"].isoformat(),
        execution_time_seconds=job["execution_time_seconds"],
        sefirot_results=sefirot,
        summary=summary
    )


@app.delete("/api/jobs/{job_id}")
async def delete_job(job_id: str):
    """Elimina job completado (cleanup)"""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    del jobs[job_id]
    return {"message": "Job deleted successfully"}


@app.get("/api/jobs")
async def list_jobs():
    """Lista todos los jobs (debug)"""
    return {
        "total": len(jobs),
        "jobs": [
            {
                "job_id": job["job_id"],
                "case_name": job["case_name"],
                "status": job["status"],
                "created_at": job["created_at"].isoformat()
            }
            for job in jobs.values()
        ]
    }


# ============================================================================
# SERVER
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("TIKUN FRAMEWORK API SERVER")
    print("=" * 80)
    print(f"Starting server...")
    print(f"API Documentation: http://localhost:8000/docs")
    print(f"Health Check: http://localhost:8000/")
    print("=" * 80)
    
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload en desarrollo
        log_level="info"
    )