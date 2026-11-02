from sentence_transformers import SentenceTransformer


def load_embedding_model():

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embedding model loaded successfully!")

    return model


def generate_embeddings(model, chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    print("Embeddings generated successfully!")

    print("Embedding shape:", embeddings.shape)

    return embeddings