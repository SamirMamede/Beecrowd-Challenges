# https://www.beecrowd.com.br/judge/pt/problems/view/1159

def main() -> None:

    def soma5Pares(x: int) -> int:
        soma = 0
        for i in range(x, x+10):
            if i % 2 == 0:
                soma += i
        return soma

    while True:
        numero = int(input())
        if numero == 0:
            break
        else:
            print(soma5Pares(numero))


if __name__ == "__main__":
    main()