from pathlib import Path


def load_documents(folder_path):

    documents = {}

    folder = Path(folder_path)

    for file_path in folder.glob("*.txt"):

        text = file_path.read_text(encoding="utf-8")

        documents[file_path.name] = text

    print(f"Total documents loaded: {len(documents)}")

    return documents