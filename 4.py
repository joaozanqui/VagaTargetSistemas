# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

faturamento = [{'estado': 'São Paulo', 'valor': 67836.43}, {'estado': 'Rio de Janeiro', 'valor': 36678.66},
               {'estado': 'Minas Gerais', 'valor': 29229.88}, {'estado': 'Espirito Santo', 'valor': 27165.48},
               {'estado': 'Outros', 'valor': 19849.53}]

total = 0
for estado in faturamento:
    valor = estado['valor']
    total += valor

for estado in faturamento:
    print(f"{estado['estado']} - {estado['valor']/total * 100}%")