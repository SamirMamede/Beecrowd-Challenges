# https://www.beecrowd.com.br/judge/pt/problems/view/1175

def main() -> None:
    lista: list[int] = []

    for _ in range(20):
        numero = int(input())
        lista.append(numero)

    lista.reverse()

    for indice, valor in enumerate(lista):
        print(f'N[{indice}] = {valor}')


if __name__ == "__main__":
    main()