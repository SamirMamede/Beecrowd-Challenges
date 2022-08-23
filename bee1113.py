# https://www.beecrowd.com.br/judge/pt/problems/view/1113

def main() -> None:

    while True:
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])

        if x == y:
            break

        if x < y:
            print('Crescente')
        else:
            print('Decrescente')


if __name__ == "__main__":
    main()