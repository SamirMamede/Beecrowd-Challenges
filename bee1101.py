# https://www.beecrowd.com.br/judge/pt/problems/view/1101

def main() -> None:

    while True:
        valores = input().strip().split()

        m = int(valores[0])
        n = int(valores[1])

        if m == 0 or n == 0 or m < 0 or n < 0:
            break

        lista = [m, n]
        lista = sorted(lista)

        soma = 0

        for i in range(lista[0], lista[1] + 1):
            print(i, end=' ')
            soma += i
        print('Sum={}' .format(soma))


if __name__ == "__main__":
    main()