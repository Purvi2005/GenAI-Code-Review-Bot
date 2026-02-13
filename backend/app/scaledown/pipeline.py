from app.scaledown.chunker import chunk_text
from app.scaledown.compressor import compress_chunk

def scaledown_diff(diff_text):
    chunks = chunk_text(diff_text)
    compressed_chunks = []
    for chunk in chunks:
        compressed_chunks.append(compress_chunk(chunk))
    return "\n".join(compressed_chunks)
