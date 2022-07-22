'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar 
os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias 
foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações
, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade 
de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas 
e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em 
relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''

n = int(input(''))
C = 0
R = 0
S = 0
for i in range(n):
    a, ch = list(map(str, input().split()))
    a = int(a)
    if(ch == 'C'):
        C += a
    elif (ch == 'R'):
        R += a
    else:
        S += a
total = C+R+S
x = (C*100.00)/total
y = (R*100.00)/total
z = (S*100.00)/total
print("Total: {} cobaias".format(total))
print("Total de coelhos:", C)
print("Total de ratos:", R)
print("Total de sapos:", S)
print("Percentual de coelhos: %.2lf %%" % x)
print("Percentual de ratos: %.2lf %%" % y)
print("Percentual de sapos: %.2lf %%" % z)
