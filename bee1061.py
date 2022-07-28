'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, 
iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o 
evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho
 a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do 
mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento 
vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra 
informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''
dia1 = int(input().split()[1])
hr1, min1, seg1 = map(int, input().split(':'))
tempo1 = seg1 + min1*60 + hr1*60*60 + dia1 *24*60*60

dia2 = int(input().split()[1])
hr2, min2, seg2 = map(int, input().split(':'))
tempo2 = seg2 + min2*60 + hr2*60*60 + dia2*24*60*60

tempo = tempo2 - tempo1
dias = tempo//(24*60*60)

tempo = tempo % (24 * 60 * 60)

horas = tempo // (60 * 60)

tempo = tempo % (60 * 60)

minutos = tempo // 60 

segundos = tempo % 60

print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")