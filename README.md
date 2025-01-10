# Retrieval-Augmented Generation (RAG) with Qdrant and Gemini

This project demonstrates how to perform Retrieval-Augmented Generation (RAG) using Qdrant for vector storage and Gemini for language generation. The setup involves loading documents, generating embeddings, storing them in Qdrant, and querying them to generate responses using Gemini.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Ingesting Documents](#ingesting-documents)
- [Running the RAG Script](#running-the-rag-script)
- [Configuration](#configuration)
- [License](#license)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/B20dact107/RAGBasic.git
    cd RAGBasic
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Setup


1. **Create a `.env` file** in the project directory and add your OpenAI API key:

    ```env
    GEMINI_KEY=your-geminigemini-api-key
    ```

## Ingesting Documents

Use the `embeddingsdata.py` script to load and process documents, generate embeddings, and store them in Qdrant.

```bash
python embeddingsdata.py
```

## Running the RAG Script
Use the `chatbot.py` script to query the vector database and generate responses using GeminiGemini.
```bash
python chatbot.py
```
## Input question and LLM is gemini
```bash
Enter your question (or 'quit' to exit): What is RAG?
Chose LLM(gemini): gemini
```

## Configuration
- Qdrant: Ensure Qdrant is running on http://localhost:6333.
- GEMINI API Key: Store your GEMINI API key in a .env file in the project directory.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
