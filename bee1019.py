'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o 
expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
segundos = int(input())

horas = segundos//(60*60)
segundos = segundos%(60*60)

minutos = segundos//60
segundos = segundos%60

print(f"{horas}:{minutos}:{segundos}")