# https://www.beecrowd.com.br/judge/pt/problems/view/1133

def main() -> None:

    x = int(input())
    y = int(input())

    lista = [x, y]
    lista = sorted(lista)

    x = lista[0]
    y = lista[1]

    for i in range(x + 1, y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)


if __name__ == "__main__":
    main()