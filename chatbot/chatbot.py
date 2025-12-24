from retrieval import retrieve_context
from llm import build_prompt, client

def chatbot(question):
    context = retrieve_context(question)

    if not context.strip():
        return "I don't know. The answer is not present in the knowledge base."

    prompt_text = build_prompt(context, question)

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt_text
    )

    if hasattr(response, "text") and response.text:
        return response.text.strip()

    return "I don't know."
