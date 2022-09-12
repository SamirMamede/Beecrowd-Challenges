# https://www.beecrowd.com.br/judge/pt/problems/view/1157

def main() -> None:

    n = int(input())

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


if __name__ == "__main__":
    main()