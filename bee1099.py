# https://www.beecrowd.com.br/judge/pt/problems/view/1099

def main() -> None:

    n = int(input())

    for i in range(n):
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])

        lista = [x, y]
        lista = sorted(lista)

        x = lista[0]
        y = lista[1]

        soma = 0

        for i in range(x + 1, y):
            if i % 2 != 0:
                soma += i

        print(soma)


if __name__ == "__main__":
    main()