'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
hr_i, min_i, hr_f, min_f = map(int, input().split(" "))

min_i += hr_i*60
min_f += hr_f*60

tempo = min_f - min_i
if tempo <= 0:
    tempo += 24*60
horas = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTOS(S)")