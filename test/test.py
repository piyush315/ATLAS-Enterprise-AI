import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Test 1: OpenAI Embeddings
embedding_response = client.embeddings.create(
    model=os.getenv("OPENAI_EMBED_MODEL"),
    input="Hello Amazon Bedrock",
    dimensions=int(os.getenv("EMBED_DIM", 1024))
)

embedding_data = embedding_response.data[0].embedding

print("Embedding dimension:", len(embedding_data))


# Test 2: OpenAI Chat Model
chat_response = client.chat.completions.create(
    model=os.getenv("OPENAI_CHAT_MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in one sentence."
        }
    ],
    max_tokens=200
)

print(
    "Nova Response:",
    chat_response.choices[0].message.content
)
