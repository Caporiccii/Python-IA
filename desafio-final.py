from contato_con_llm import recebe_linha_e_retorna_json
import json
import re

lista_de_resenhas = []

with open ("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)

    # Tenta extrair apenas o trecho de JSON da resposta do modelo,
    # ignorando qualquer texto extra antes/depois.
    match = re.search(r"\{.*\}|\[.*\]", resenha_json, re.DOTALL)
    if not match:
        print("Resposta sem JSON válido, pulando:", resenha_json)
        continue

    try:
        resenha_dict = json.loads(match.group(0))
    except json.JSONDecodeError as e:
        print("Falha ao decodificar JSON, pulando:", e, "\nResposta:", resenha_json)
        continue

    lista_de_resenhas_json.append(resenha_dict)

def contador_e_juntador(lista_de_dicionarios):
    contador_de_positivas = 0
    contador_de_negativas = 0
    contador_de_neutra = 0
    lista_de_dicionarios_str = []

    for dicionario in lista_de_dicionarios:
         if dicionario["classificacao"] == "positiva":
             contador_de_positivas += 1
         elif dicionario["classificacao"] == "negativa":
             contador_de_negativas += 1
         else:
           contador_de_neutra += 1

         lista_de_dicionarios_str.append(str(dicionario))  
           
         textos_unidos = "####".join(lista_de_dicionarios_str)

    return contador_de_positivas, contador_de_negativas, contador_de_neutra, textos_unidos

pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)

print(f"Positivas: {pos}\n")
print(f"Negativas: {neg}\n")
print(f"Neutras: {neut}\n")
print(textos)