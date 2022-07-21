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