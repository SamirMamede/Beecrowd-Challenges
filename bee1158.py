# https://www.beecrowd.com.br/judge/pt/problems/view/1158

def main() -> None:

    n = int(input())
    valor = 0

    for i in range(n):
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])
        s = 0

        for j in range(y):
            while x % 2 == 0:
                x += 1
            s += x
            x += 1
        print(s)


if __name__ == "__main__":
    main()