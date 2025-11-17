from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    # You can replace the model with any local Ollama embedding model
    return OllamaEmbeddings(model="nomic-embed-text")
