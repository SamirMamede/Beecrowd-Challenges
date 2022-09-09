# # https://www.beecrowd.com.br/judge/pt/problems/view/1134

def main() -> None:

    alcool = gasolina = diesel = 0
    lista = [1, 2, 3, 4]

    while True:
        resposta = 0
        while resposta not in lista:
            resposta = int(input())
        if resposta == 1:
            alcool += 1
        elif resposta == 2:
            gasolina += 1
        elif resposta == 3:
            diesel += 1
        else:
            break

    print('MUITO OBRIGADO')
    print(f'Alcool: {alcool}')
    print(f'Gasolina: {gasolina}')
    print(f'Diesel: {diesel}')


if __name__ == "__main__":
    main()