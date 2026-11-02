def recursive_chunk(text, chunk_size=45, overlap=10):

    separators = ["\n\n", "\n", ". ", "? ", "! ", "; ", ", ", " "]

    pieces = [text]

    for sep in separators:

        new_pieces = []

        for piece in pieces:

            if len(piece.split()) > chunk_size:

                parts = [p.strip() for p in piece.split(sep) if p.strip()]

                new_pieces.extend(parts if len(parts) > 1 else [piece])

            else:

                new_pieces.append(piece)

        pieces = new_pieces

    packed = []
    current = []

    for piece in pieces:

        words = piece.split()

        while len(words) > chunk_size:

            if current:
                packed.append(" ".join(current))
                current = []

            packed.append(" ".join(words[:chunk_size]))

            words = words[chunk_size:]

        if words and len(current) + len(words) > chunk_size:

            packed.append(" ".join(current))

            current = []

        current.extend(words)

    if current:
        packed.append(" ".join(current))

    # Add overlap

    if overlap > 0 and len(packed) > 1:

        overlapped = [packed[0]]

        for chunk in packed[1:]:

            previous_words = overlapped[-1].split()

            prefix = previous_words[-overlap:]

            overlapped.append(
                " ".join(prefix + chunk.split())
            )

        packed = overlapped

    return [p for p in packed if p.strip()]


def build_chunks_from_dict(documents, chunk_size=45, overlap=10):

    rows = []

    for filename, text in documents.items():

        chunks = recursive_chunk(text, chunk_size, overlap)

        for index, chunk in enumerate(chunks, start=1):

            rows.append({

                "source": filename,

                "chunk_id": index,

                "text": chunk

            })

    return rows