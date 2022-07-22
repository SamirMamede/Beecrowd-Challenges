'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. 
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos 
ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
'''
eixos = list(map(lambda x: float(x), input().split(" ")))

eixo_x, eixo_y = eixos[0], eixos[1]

if(eixo_x > 0 and eixo_y > 0):
    print("Q1")
elif(eixo_x > 0 and eixo_y < 0):
    print("Q4")
elif(eixo_x < 0 and eixo_y > 0):
    print("Q2")
elif(eixo_x < 0 and eixo_y < 0):
    print("Q3")
elif(eixo_x == 0 and eixo_y == 0):
    print("Origem")
elif(eixo_x == 0 and eixo_y > 0 or eixo_x == 0 and eixo_y < 0):
    print("Eixo Y")
elif(eixo_y == 0 and eixo_x > 0 or eixo_y == 0 and eixo_x < 0):
    print("Eixo X")