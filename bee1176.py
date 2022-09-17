# https://www.beecrowd.com.br/judge/pt/problems/view/1176

def main() -> None:
    total = 61
    fibonacci = [0, 1]
    a, b = fibonacci

    for _ in range(2, total):
        c = a + b
        fibonacci.append(c)
        a, b = b, c

    testes = int(input())

    for _ in range(testes):
        index = int(input())
        print(f'Fib({index}) = {fibonacci[index]}')


if __name__ == "__main__":
    main()