import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


def semantic_search(query, model, chunks, embeddings, top_k=3):

    # Convert query into embedding

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Calculate similarity

    scores = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    # Get top matching chunks

    top_indices = np.argsort(scores)[::-1][:top_k]

    print("\nSearch Results:")

    for rank, idx in enumerate(top_indices, 1):

        item = chunks[idx]

        print(
            f"\n{rank}. {item['source']} "
            f"| Chunk {item['chunk_id']} "
            f"| Similarity: {scores[idx]:.4f}"
        )

        print(item["text"])