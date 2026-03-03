from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI(title="Azure Multi-modal Compliance Engine")

class AuditRequest(BaseModel):
    video_url: str

@app.post("/audit")
async def trigger_audit(request: AuditRequest, background_tasks: BackgroundTasks):
    """Trigger a compliance audit for a given video URL."""
    # TODO: Kick off LangGraph workflow in background
    return {"status": "Audit triggered", "video_url": request.video_url}

@app.get("/status/{audit_id}")
async def get_status(audit_id: str):
    """Check the status of an audit."""
    return {"audit_id": audit_id, "status": "In Progress"}
