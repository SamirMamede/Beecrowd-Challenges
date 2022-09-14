# https://www.beecrowd.com.br/judge/pt/problems/view/1160

def main() -> None:

    n = int(input())

    for i in range(n):
        valores = input().strip().split()

        a = int(valores[0])
        b = int(valores[1])
        ca = float(valores[2])
        cb = float(valores[3])

        anos = 0

        while a <= b:

            crescimentoa = ca / 100 * a
            crescimentob = cb / 100 * b

            a = int(a + crescimentoa)
            b = int(b + crescimentob)
            anos += 1
            if anos > 100:
                print('Mais de 1 seculo.')
                break
        if anos <= 100:
            print(f'{anos} anos.')


if __name__ == "__main__":
    main()