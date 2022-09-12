# https://www.beecrowd.com.br/judge/pt/problems/view/1153

def main() -> None:

    n = int(input())

    if 0 < n < 13:
        for i in range(n, 1, -1):
            n *= i - 1
        fatorial = n
        print(fatorial)


if __name__ == "__main__":
    main()