soma = 0
quantidade = 0

for i in range(6):
    valor = float(input())
    if valor > 0:
        soma += valor
        quantidade += 1
print(f'{quantidade} valores positivos')
print(f'{soma/quantidade :.1f}')
