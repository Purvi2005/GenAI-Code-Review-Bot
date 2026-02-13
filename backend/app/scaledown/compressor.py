from app.ai.gemini_client import generate_response

def compress_chunk(chunk):
    prompt = f"""
    Compress the following code diff.
    Preserve logic and intent.
    Remove redundancy and boilerplate.
    Output concise technical summary.

    {chunk}
    """
    return generate_response(prompt)
