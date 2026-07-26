import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from rag_chain import ask_naranjito_with_details, stream_naranjito_with_details

app = FastAPI(
    title="Naranjito RAG API",
    description="Servidor Backend RAG para consultas vectoriales sobre la memoria técnica del TFG (OVOD - UPV).",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str = Field(..., example="¿Qué modelo destacó entre las arquitecturas de vocabulario abierto?")
    chat_history: Optional[List[str]] = Field(default_factory=list, description="Lista de preguntas previas para evitar repeticiones en las sugerencias.")

class QueryResponse(BaseModel):
    answer: str
    suggestions: List[str] = Field(default_factory=list)

@app.get("/")
def home():
    return {
        "status": "ok", 
        "service": "Servidor Naranjito RAG", 
        "pinecone_index": os.getenv("PINECONE_INDEX_NAME", "ovod-tfg")
    }

@app.post("/ask", response_model=QueryResponse)
@app.post("/chat", response_model=QueryResponse)
def chat_endpoint(request: QueryRequest):
    user_query = request.question.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía.") 
    try:
        rag_output = ask_naranjito_with_details(
            question=user_query, 
            chat_history=request.chat_history
        )
        return QueryResponse(
            answer=rag_output["answer"],
            suggestions=rag_output.get("suggestions", [])
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error al consultar el RAG sobre Pinecone: {str(e)}"
        )

@app.post("/ask/stream")
@app.post("/chat/stream")
def chat_stream_endpoint(request: QueryRequest):
    user_query = request.question.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía.")
    return StreamingResponse(
        stream_naranjito_with_details(
            question=user_query,
            chat_history=request.chat_history
        ),
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)