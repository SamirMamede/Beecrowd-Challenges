'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição 
dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

# Usando lista

#entrada = []
#for i in range(100):
#    user = int(input())
#    entrada.append(user)

#maior = max(entrada) 
#posicao = entrada.index(maior)

#print(maior)
#print(posicao+1)

maior = - 9999999999
for i in range(100):
    n = int(input())
    if n > maior :
        maior = n
        posicao = i

print(maior)
print(posicao+1)