from itertools import count
from openai import OpenAI
import json

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
    model = "google/gemma-3-4b",
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
   return response.choices[0].message.content.strip().replace("```json", "").replace("```", "")
   

dict_classify = json.loads(classify_review(revies_list))

def cout_classification(dict_classify):
    list_positive = []
    list_negative = []
    list_neutral = []

    for review in dict_classify:
        if review["classificacao"] == "positiva":
            list_positive.append(review["classificacao"])
        elif review["classificacao"] == "negativa":
                list_negative.append(review["classificacao"])               
        else:
            list_neutral.append(review["classificacao"])
            return list_negative, list_neutral, list_positive


list_positive, list_negative, list_neutral = cout_classification(dict_classify)

dict_count = {
    "positivas": len(list_positive),
    "negativas": len(list_negative),
    "neutras": len(list_neutral)
}

def join_reviews(dict_classify, separator="----"):
    reviews_text = []
    for review in dict_classify:
        review_str = f"Usuário: {review['usuario']}\nResenha: {review['resenha_pt']}\n"
        reviews_text.append(review_str)
    
    return separator.join(reviews_text)

def join_and_return_all(dict_classify, separator="----"):
    
    return f"Classificacao: {dict_count},\n Resenhas: {join_reviews(dict_classify, separator)}"

print(join_and_return_all(dict_classify))