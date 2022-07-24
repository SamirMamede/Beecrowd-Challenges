'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou 
"Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
'''

entrada = list(map(int, input().split(" ")))

a, b = entrada[0], entrada[1]
resto = max(a, b) % min(a, b)

if resto == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
