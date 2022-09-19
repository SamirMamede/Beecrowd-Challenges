# https://www.beecrowd.com.br/judge/pt/problems/view/1858

def main() -> None:
    n = int(input())

    numeros: list[int] = [int(x) for x in input().split()]

    print(numeros.index(min(numeros)) + 1)


if __name__ == "__main__":
    main()