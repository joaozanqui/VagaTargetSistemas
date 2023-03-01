import json

with open('dados.json', 'r') as f:
    faturamento = json.load(f)

print(faturamento)

menor = float('inf')
maior = float('-inf')
total = 0
diasAcimaDaMedia = 0
diasComFaturamento = 0

for dia in faturamento:
    valor = dia['valor']
    if(valor != 0):
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        diasComFaturamento += 1
        total += valor

for dia in faturamento:
    if dia['valor'] > (total / diasComFaturamento) and dia['valor'] > 0:
        diasAcimaDaMedia += 1

print(f"Menor valor de faturamento diário: {menor}")
print(f"Maior valor de faturamento diário: {maior}")
print(f"Número de dias com faturamento diário acima da média mensal: {diasAcimaDaMedia}")