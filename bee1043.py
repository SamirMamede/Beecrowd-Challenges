'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, 
calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''

entrada = list(map(float, input().split(" ")))

a, b, c = entrada[0], entrada[1], entrada[2]

if a + b == c or a + c == b or b + c == a:
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
elif a + b > c or a + c > b or b + c > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")