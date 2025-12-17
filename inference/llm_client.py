from openai import OpenAI
client = OpenAI()

def generate(user_query: str) -> str:
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=[
        {"role":"user","content":user_query}
    ])
    return response.choices[0].message.content