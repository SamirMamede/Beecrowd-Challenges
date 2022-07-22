'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. 
Em seguida, informe à qual cidade o DDD pertence.

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD 
correspondente ao número digitado.
'''

codigo = int(input(''))

if codigo == 61:
    print('Brasilia')
elif codigo == 71:
    print('Salvador')
elif codigo == 11:
    print('Sao Paulo')
elif codigo == 21:
    print('Rio de Janeiro')
elif codigo == 32:
    print('Juiz de Fora')
elif codigo == 19:
    print('Campinas')
elif codigo == 27:
    print('Vitoria')
elif codigo == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
