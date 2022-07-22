'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

while True:
    num = list(map(int, input().split()))
    tamanholista = len(num)
    if tamanholista > 3:
        continue
    elif tamanholista < 3:
        continue
    else:
        print(f'{max(num)} eh o maior')
        break