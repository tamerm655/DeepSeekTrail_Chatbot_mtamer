from config import llm

def generate_response(query, retrieved_chunks):
    """Generates a response using retrieved text."""
    if not retrieved_chunks:
        return "No relevant information found."

    prompt = f"""
    You are an AI assistant helping to answer questions based on provided document excerpts.
    
    **Question:** {query}
    
    **Relevant Information from Documents:**
    {retrieved_chunks}
    
    **Instructions:**
    - Analyze the query and understand the intent.
    - Use the provided document excerpts to answer the question.
    - If the answer is explicitly in the text, return it directly.
    """

    response = llm.invoke(prompt)

    print("🤖 LLM Prompt:", prompt)
    print("💬 LLM Response:", response)

    return response
