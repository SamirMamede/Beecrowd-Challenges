# https://www.beecrowd.com.br/judge/pt/problems/view/1150

def main() -> None:

    x = int(input())
    z = int(input())
    while z <= x:
        z = int(input())

    numerosSomados = 1
    soma = x
    i = x + 1

    while soma <= z:
        soma += i
        numerosSomados += 1
        i += 1

    print(numerosSomados)


if __name__ == "__main__":
    main()