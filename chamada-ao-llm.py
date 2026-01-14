from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

respota_do_llm =  client_openai.chat.completions.create(
    model="google/gemma-3-4b",
    messages=[
        {"role": "system", "content": "Voce e um agente de IA que sempre responde de forma muito sarcastica"},
        {"role": "user", "content": "O que e IA generativa?"}
    ],
    temperature=1.0,
)

print(respota_do_llm.choices[0].message.content)