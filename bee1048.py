salario = float(input())

'''
if salario > 0 and salario <= 400:
    novo_salario = salario * 15 / 100 + salario
    reajuste = salario * 15 / 100
    percentual = 15
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario > 400 and salario <= 800:
    novo_salario = salario * 12 / 100 + salario
    reajuste = salario * 12 / 100
    percentual = 12
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario > 800 and salario <= 1200:
    novo_salario = salario * 10 / 100 + salario
    reajuste = salario * 10 / 100
    percentual = 10
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario > 1200 and salario <= 2000:
    novo_salario = salario * 7 / 100 + salario
    reajuste = salario * 7 / 100
    percentual = 7
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
else:
    novo_salario = salario * 4 / 100 + salario
    reajuste = salario * 4 / 100
    percentual = 4
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
'''
if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual / 100
novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}\n"
      f"Reajuste ganho: {reajuste:.2f}\n"
      f"Em percentual: {percentual} %"
)