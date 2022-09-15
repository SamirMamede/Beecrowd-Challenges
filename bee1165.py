# https://www.beecrowd.com.br/judge/pt/problems/view/1165

def main() -> None:

    n = int(input())

    for i in range(n):

        divisivel = 0
        x = int(input())

        for k in range(1, x + 1):
            if x % k == 0:
                divisivel += 1
        if divisivel == 2:
            print(f'{x} eh primo')
        else:
            print(f'{x} nao eh primo')


if __name__ == "__main__":
    main()