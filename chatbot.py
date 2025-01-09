from sentence_transformers import SentenceTransformer
from langchain_qdrant import Qdrant 
from qdrant_client import QdrantClient
from gemini import GeminiLLM

embeddings = SentenceTransformer( 'paraphrase-MiniLM-L6-v2')

def embedding_function(text):
    if isinstance(text, str):
        text = [text]
    return embeddings.encode(text)[0].tolist()

qdrant_client = QdrantClient("localhost", port=6333)

vectorstore = Qdrant(client = qdrant_client,
                     collection_name = "document_collection",
                     embeddings = embedding_function,
                     vector_name = "content" 
                     )

retriever = vectorstore.as_retriever(search_kwargs = {"k" : 2})

template = """
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.

Context : {context}

Question : {question}

Answer:
"""
gemini_llm = GeminiLLM()

def get_response(question , llm_choice):
    docs = retriever.get_relevant_documents(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = template.format(context = context, question =question)

    if llm_choice.lower() == 'gemini' :
        response = gemini_llm.generate_response(prompt)
    else:
        response = "invalid LLM choice "
    return context,response

if __name__ == "__main__":
    while True:
            question = input("Enter your question (or 'quit' to exit): ")
            if question.lower() == 'quit':
                 break
            llm_choice = input("Chose LLM(gemini): ")
            context,response = get_response(question, llm_choice)
            print(f"\n Question : {question}")
            print(f"Context : {context}")
            print(f"Answer ({llm_choice}) : {response}\n")
