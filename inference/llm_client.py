from openai import OpenAI
client = OpenAI()

def generate(prompt):
    return client.chat.completions.create(model= "gpt-4.1-mini", messages=prompt, stream=True)