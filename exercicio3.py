
import json

# Carregar os dados do arquivo JSON
with open("dados.json", encoding="utf-8") as meu_json:
    dados = json.load(meu_json)

# Extrair os valores e encontrar o maior
valores = [item["valor"] for item in dados]
maior_valor = max(valores)
minimo_valor = min(valores)
soma = sum(valores)
media = (soma / (len(valores)-9))

maiorQueMedia = [item["dia"] for item in dados if item["valor"] > media]
diaValorMinimo= [item["dia"] for item in dados if item["valor"] == minimo_valor]

print("a media dos valores é "+ str(media)) 
print("O maior valor é ", maior_valor)
print("O valor minimo é "+ str(minimo_valor))
print("O dia com valor minimo"+str(diaValorMinimo))
print(" dias que os valores foram maior que a media"+ str(maiorQueMedia))


