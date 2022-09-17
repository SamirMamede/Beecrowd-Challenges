# https://www.beecrowd.com.br/judge/pt/problems/view/1179

def main() -> None:

    par: list[int] = []
    impar: list[int] = []

    for _ in range(15):
        valor = int(input())

        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)

        if len(par) == 5:
            for index_par, valor_par in enumerate(par):
                print(f'par[{index_par}] = {valor_par}')
            par = []
        if len(impar) == 5:
            for index_impar, valor_impar in enumerate(impar):
                print(f'impar[{index_impar}] = {valor_impar}')
            impar = []

    for index_impar_1, valor_impar_1 in enumerate(impar):
        print(f'impar[{index_impar_1}] = {valor_impar_1 }')

    for index_par_1, valor_par_1 in enumerate(par):
        print(f'par[{index_par_1 }] = {valor_par_1 }')


if __name__ == "__main__":
    main()