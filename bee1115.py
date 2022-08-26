# https://www.beecrowd.com.br/judge/pt/problems/view/1115

def main() -> None:

    while True:
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])

        if x == 0 or y == 0:
            break
        elif x > 0 and y > 0:
            print('primeiro')
        elif x < 0 and y > 0:
            print('segundo')
        elif x < 0 and y < 0:
            print('terceiro')
        else:
            print('quarto')


if __name__ == "__main__":
    main()