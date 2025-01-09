import os
from uuid import uuid4

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

MODEL = 'paraphrase-MiniLM-L6-v2'
embeddings = SentenceTransformer(MODEL)

data_folder = "storage"
documents = []
for filename in os.listdir(data_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(data_folder, filename)
        loader = PyPDFLoader(pdf_path)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
        documents.extend(loader.load_and_split(text_splitter))

print(f"Number of documents: {len(documents)}")

client = QdrantClient("localhost", port=6333, timeout=1200)

if not client.collection_exists("document_collection"):
    client.create_collection(
        collection_name="document_collection",
          vectors_config={
        "content": VectorParams(size=384, distance=Distance.COSINE),
    },
    )

def chunked_metadata(data, client=client, collection_name="document_collection", batch_size=100):
    chunked_metadata = []
    for item in data:
        id = str(uuid4())
        content = item.page_content
        source = item.metadata.get("source", "unknown")
        page = item.metadata.get("page", 0)

        content_vector = embeddings.encode([content])[0]
        payload = {
            "page_content": content,
            "metadata": {
                "source": source,
                "page": page,
            },
        }

        metadata = PointStruct(
            id=id,
            vector={"content": content_vector},
            payload=payload,
        )
        chunked_metadata.append(metadata)

        if len(chunked_metadata) >= batch_size:
            client.upsert(
                collection_name=collection_name,
                points=chunked_metadata,
            )
            chunked_metadata = []

    if chunked_metadata:
        client.upsert(
            collection_name=collection_name,
            points=chunked_metadata,
        )

chunked_metadata(documents)

collection_info = client.get_collection("document_collection")
print(f"Points in collection: {collection_info.points_count}")
