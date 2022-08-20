# https://www.beecrowd.com.br/judge/pt/problems/view/1097

I, J = 1, 7

while I <= 9:
    flag = J - 3
    while J != flag:
        print(f'I={I} J={J}')
        J -= 1
    I += 2
    J += 5