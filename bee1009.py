nome = str(input(''))
salario_fixo = float(input(''))
vendas_efet = float(input(''))
total = (vendas_efet * 15) / 100 + salario_fixo
print(f'TOTAL = R$ {total:.2f}')
