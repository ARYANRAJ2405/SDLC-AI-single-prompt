from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import tempfile
import shutil
from datetime import datetime
import sys
import logging

from dotenv import load_dotenv

# Setup imports from local modules
_pkg_dir = Path(__file__).resolve().parent
if str(_pkg_dir) not in sys.path:
    sys.path.insert(0, str(_pkg_dir))

from config import Settings
from graph import build_graph
from models import BRDState

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="BRD Generation API",
    description="Generate Business Requirements Documents from meeting transcripts",
    version="1.0.0"
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store for tracking job status
jobs = {}


@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "BRD Generation API",
        "docs": "/docs",
        "endpoints": {
            "generate": "/generate",
            "status": "/status/{job_id}",
            "health": "/health"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/generate")
async def generate_brd(
    files: list[UploadFile] = File(...),
    background_tasks: BackgroundTasks = None
):
    """
    Generate BRD from uploaded files
    
    - **files**: List of transcript and supporting document files
    
    Returns: Job ID to track progress, or directly return the generated BRD
    """
    try:
        # Create temporary directory for uploads
        temp_dir = tempfile.mkdtemp()
        file_paths = []
        
        # Save uploaded files
        for file in files:
            file_path = Path(temp_dir) / file.filename
            with open(file_path, "wb") as f:
                content = await file.read()
                f.write(content)
            file_paths.append(str(file_path))
        
        # Create output directory
        settings = Settings()
        output_dir = Path(settings.default_output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_md = str(output_dir / f"brd_{timestamp}.md")
        output_docx = str(output_dir / f"brd_{timestamp}.docx")
        
        # Generate BRD
        graph = build_graph().compile()
        state = BRDState(
            inputs=file_paths,
            output_markdown_path=output_md,
            output_docx_path=output_docx,
        )
        
        # Run the graph
        result = graph.invoke(state)
        
        # Cleanup temp directory
        shutil.rmtree(temp_dir)
        
        return {
            "status": "success",
            "message": "BRD generated successfully",
            "output_markdown": output_md,
            "output_docx": output_docx,
            "timestamp": timestamp
        }
        
    except Exception as e:
        logger.error(f"Error generating BRD: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )


@app.get("/download/{file_type}/{timestamp}")
async def download_brd(file_type: str, timestamp: str):
    """
    Download generated BRD file
    
    - **file_type**: 'markdown' or 'docx'
    - **timestamp**: File timestamp from generation response
    """
    try:
        settings = Settings()
        output_dir = Path(settings.default_output_dir)
        
        if file_type == "markdown":
            file_path = output_dir / f"brd_{timestamp}.md"
            media_type = "text/markdown"
        elif file_type == "docx":
            file_path = output_dir / f"brd_{timestamp}.docx"
            media_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        else:
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid file_type. Use 'markdown' or 'docx'"}
            )
        
        if not file_path.exists():
            return JSONResponse(
                status_code=404,
                content={"error": "File not found"}
            )
        
        return FileResponse(file_path, media_type=media_type)
        
    except Exception as e:
        logger.error(f"Error downloading file: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
