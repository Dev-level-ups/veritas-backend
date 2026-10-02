import re
import uuid
from typing import Annotated

from fastapi import APIRouter, UploadFile, File, HTTPException
from supabase_client import supabase

router = APIRouter(prefix="/documents", tags=["Documents"])

MAX_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post(
    "/upload",
    responses={
        400: {"description": "Not a PDF, or file is larger than 10 MB"},
        500: {"description": "Failed to upload the PDF to storage"},
    },
)
async def upload_document(file: Annotated[UploadFile, File()]):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Only PDF files are allowed.")

    file_bytes = await file.read()
    if len(file_bytes) > MAX_SIZE:
        raise HTTPException(400, "PDF must be smaller than 10 MB.")

    safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", file.filename or "document.pdf")
    file_path = f"uploads/{uuid.uuid4().hex}_{safe_name}"

    try:
        supabase.storage.from_("documents").upload(
            file_path,
            file_bytes,
            {"content-type": "application/pdf"},
        )
    except Exception as e:
        raise HTTPException(500, f"Failed to upload PDF: {e}")

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "path": file_path,
    }