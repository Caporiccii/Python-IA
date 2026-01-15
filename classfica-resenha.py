from openai import OpenAI

client_openai = OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
    )

revies_list = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as review:
    for line in review:
        revies_list.append(line.strip())

def classify_review(reviews):
   response = client_openai.chat.completions.create(
    model = "google/gemma-3-1b",
    messages=[
        {"role": "system", "content":"Você e um agente de IA que classifica as resenhas de aplicativos de qualquer loja"},
        {"role": "user", "content": f"""Vou lhe passar uma serie de resenhas sobre o ChatGPT, classificara como (positiva, negativa
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

        Aqui esta a lista de resenhas:{reviews}

        '"""}
    ]
   )
   json = response
   print (json) 

classify_review(revies_list)