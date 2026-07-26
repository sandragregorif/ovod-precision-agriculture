import os
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

import re
from pinecone import Pinecone

load_dotenv()

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "ovod-tfg")


def index_documents():
    pinecone_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_key:
        raise ValueError("No se encontró la variable PINECONE_API_KEY en el archivo .env")

    print("1. Cargando documentos desde docs/...")
    
    pdf_loader = DirectoryLoader(DOCS_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader)
    md_loader = DirectoryLoader(
        DOCS_DIR, 
        glob="**/*.md", 
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    
    raw_pdf_docs = pdf_loader.load()
    print(f"Páginas PDF cargadas originalmente: {len(raw_pdf_docs)}")
    
    filtered_pdf_docs = []
    skipped_count = 0
    for doc in raw_pdf_docs:
        text_lower = doc.page_content.lower()
        page_num = doc.metadata.get("page", 0) + 1
        
        # 1. Detectar índices y listas de tablas/figuras
        dots_count = text_lower.count(". . .")
        if dots_count > 5:
            skipped_count += 1
            print(f"Omitiendo página {page_num} (detección de índice por puntos líderes)")
            continue
            
        index_keywords = ["índice de tablas", "índice de figuras", "índice general", "table of contents", "list of tables", "list of figures"]
        if any(kw in text_lower for kw in index_keywords) and page_num <= 20:
            skipped_count += 1
            print(f"Omitiendo página {page_num} (palabra clave de índice)")
            continue
            
        # 2. Detectar páginas de bibliografía/referencias al final de la tesis
        if page_num > 100:
            citations_count = len(re.findall(r'\[\d+\]', text_lower))
            if citations_count > 5:
                skipped_count += 1
                print(f"Omitiendo página {page_num} (bibliografía por patrón de citas [{citations_count}])")
                continue
            if "bibliografía" in text_lower or "references" in text_lower or "bibliography" in text_lower:
                skipped_count += 1
                print(f"Omitiendo página {page_num} (palabra clave de referencias)")
                continue

        filtered_pdf_docs.append(doc)
        
    print(f"Páginas PDF filtradas: {len(filtered_pdf_docs)} (Omitidas: {skipped_count})")
    
    md_docs = md_loader.load()
    print(f"Documentos Markdown cargados: {len(md_docs)}")
    
    all_docs = filtered_pdf_docs + md_docs
    print(f"Total documentos a procesar: {len(all_docs)}")
    
    print("2. Dividiendo en fragmentos (chunks)...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=250)
    splits = text_splitter.split_documents(all_docs)
    
    print("3. Generando Embeddings de Hugging Face...")
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small",
        encode_kwargs={'normalize_embeddings': True}
    )
    
    print("4. Borrando el índice existente en Pinecone...")
    try:
        pc = Pinecone(api_key=pinecone_key)
        index = pc.Index(PINECONE_INDEX_NAME)
        index.delete(delete_all=True)
        print("Índice de Pinecone limpiado con éxito.")
    except Exception as e:
        print(f"Advertencia al limpiar el índice: {e}")
        
    print("5. Subiendo nuevos vectores a Pinecone...")
    PineconeVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        index_name=PINECONE_INDEX_NAME,
        pinecone_api_key=pinecone_key
    )
    print("Indexación completada con éxito.")


if __name__ == "__main__":
    index_documents()