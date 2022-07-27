'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos 
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

positivos = 0
for i in range(6):
    if float(input()) > 0:
        positivos += 1
print(f"{positivos} valores positivos")

#contador = 0
#positivos = 0
#while contador < 6:
#    valor = float(input())
#    contador +=1
#    if valor >0:
#        positivos += 1
#print(f"{positivos} valores positivos")