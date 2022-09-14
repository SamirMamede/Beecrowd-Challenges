# https://www.beecrowd.com.br/judge/pt/problems/view/1164

def main() -> None:

    n = int(input())

    for i in range(n):
        x = int(input())
        soma = 0

        for i in range(1, x):
            if x % i == 0:
                soma += i
        if soma == x:
            print(f'{x} eh perfeito')
        else:
            print(f'{x} nao eh perfeito')


if __name__ == "__main__":
    main()