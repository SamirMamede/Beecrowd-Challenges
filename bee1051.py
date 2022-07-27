'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, 
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em 
benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a 
faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo 
fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 
no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, 
com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".
'''

salario = float(input())

if salario >= 0 and salario <= 2000:
    print("Isento")
elif salario > 2000 and salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario > 3000 and salario <= 4500:
    imposto = (salario - 3000) * 0.18 + 1000 * 0.08
    print(f"R$ {imposto:.2f}")
elif salario > 4500:
    imposto = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {imposto:.2f}")