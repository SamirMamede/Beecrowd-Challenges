# https://www.beecrowd.com.br/judge/pt/problems/view/1132

def main() -> None:

    soma = 0
    x = int(input())
    y = int(input())

    lista = [x, y]
    lista = sorted(lista)

    x = lista[0]
    y = lista[1]

    for i in range(x, y + 1):
        if i % 13 != 0:
            soma += i
    print(soma)


if __name__ == "__main__":
    main()