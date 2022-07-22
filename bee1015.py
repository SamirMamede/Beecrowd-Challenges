'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
calcule a distância entre eles, mostrando 4 casas decimais após a vírgula.

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e
 a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''
from math import sqrt
p1 = input('').split()
p2 = input('').split()
distancia = sqrt(((float(p2[0])) - float(p1[0]))**2 +
                 (float(p2[1]) - float(p1[1]))**2)
print(f'{distancia:.4f}')
