# https://www.beecrowd.com.br/judge/pt/problems/view/1143

def main() -> None:

    n = int(input())
    x = 1

    for i in range(n):
        print(f'{x} {x**2} {x**3}')
        x += 1


if __name__ == "__main__":
    main()