'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem 
correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
'''
import math

try:
    a, b, c = map(float, input().split(" "))

    delta = b * b - 4 * a * c
    delta = math.sqrt(delta)

    r1 = (-b + delta) / (2 * a)
    r2 = (-b - delta) / (2 * a)

    print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
except:
    print("Impossivel calcular")