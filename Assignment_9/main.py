from Document_loader import load_documents

from chunking import build_chunks_from_dict

from Embedding import load_embedding_model, generate_embeddings

from Search import semantic_search


# Step 1: Load documents

documents = load_documents("documents")


# Step 2: Load embedding model

model = load_embedding_model()


# Step 3: Create chunks

chunks = build_chunks_from_dict(
    documents,
    chunk_size=45,
    overlap=10
)

print("Total chunks:", len(chunks))





# Step 4: Generate embeddings

embeddings = generate_embeddings(model, chunks)


# Step 5: Search loop

while True:

    query = input("\nEnter your query (type exit to stop): ")

    if query.lower() == "exit":

        print("Thank you for using Semantic Search Engine!")

        break

    semantic_search(
        query,
        model,
        chunks,
        embeddings,
        top_k=3
    )