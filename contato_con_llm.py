from openai import OpenAI

client_openai = OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio"
)
    
def recebe_linha_e_retorna_json(linha):
   response = client_openai.chat.completions.create(
    model = "google/gemma-3-4b",
    messages=[
        {"role": "system", "content":f"""Vou lhe passar uma serie de resenhas sobre o ChatGPT, classificara como (positiva, negativa
        ou neutra), alem disso, vai retornar todas as resenhas classificadas, em formato JSON que seguira esse modelo
        
        'usuario' = 'contendo o nome do usuario que fez a resenha',
        'resenha_original' = 'contento a resenha pura e sem traducao', 
        'resenha_pt' = 'contento a resenha traduzida para o portugues',
        'classificacao' = 'classificacao da resenha como positiva, negativa ou neutra
        
        Exemplo de Json:
        '{{
                'usuario': 'Habimana Therese',
                'resenha_original': 'This app is very important but sometimes it gives lies',
                'resenha_pt': 'Esta aplicacao e muito importante, mas as vezes ela da mentiras',
                'classificacao': 'positiva'
        }}'

        '"""},

        {"role": "user", "content": f"Resenha: {linha}"}
    ],
    temperature=0.0
   )
   return response.choices[0].message.content.replace("```json", "").replace("```", "")
