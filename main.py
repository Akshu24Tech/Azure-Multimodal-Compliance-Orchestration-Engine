import argparse
import asyncio
from app.orchestration.workflow import WorkflowBuilder

async def run_audit(url: str):
    print(f"Starting compliance audit for: {url}")
    builder = WorkflowBuilder()
    app = builder.build()
    
    initial_state = {
        "video_url": url,
        "transcription": "",
        "ocr_text": "",
        "audit_results": {},
        "compliance_rules": []
    }
    
    async for event in app.astream(initial_state):
        for node_name, state in event.items():
            print(f"Node '{node_name}' completed.")
    
    print("Audit completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Azure Multi-modal Compliance CLI")
    parser.add_argument("--url", type=str, required=True, help="YouTube video URL to audit")
    args = parser.parse_args()
    
    asyncio.run(run_audit(args.url))
