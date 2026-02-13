def chunk_text(text, max_lines=100):
    lines = text.splitlines()
    chunks = []
    for i in range(0, len(lines), max_lines):
        chunks.append("\n".join(lines[i:i + max_lines]))
    return chunks
