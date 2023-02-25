import json


with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

dias = len(faturamento)

soma = sum(faturamento.values())

media = soma / dias

menor = min(faturamento.values())

maior = max(faturamento.values())

dias_acima_da_media = len([f for f in faturamento.values() if f > media])



print(f"Menor faturamento diário: {menor}")
print(f"Maior faturamento diário: {maior}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
