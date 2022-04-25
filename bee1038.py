lista = [[1, 4.00], [2, 4.50], [3, 5.00], [4, 2.00], [5, 1.50]]
user = input('').split()
codigo = int(user[0])
quantidade = int(user[1])

x = 0
for i in lista:
    if codigo == lista[x][0]:
        print(f'Total: R$ {quantidade*lista[x][1]:.2f}')
        break
    x += 1
