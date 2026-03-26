import os
from openai import OpenAI

OPENAI_KEY = os.environ.get("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

def summarize(text):
    prompt = f"다음 뉴스 내용을 2문장으로 요약해줘:\n{text}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
