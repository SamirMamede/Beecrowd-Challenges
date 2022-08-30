# https://www.beecrowd.com.br/judge/pt/problems/view/1116

def main() -> None:

    n = int(input())

    for i in range(n):
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])

        if y == 0:
            print('divisao impossivel')
        else:
            div = x / y
            print(div)


if __name__ == "__main__":
    main()