# https://www.beecrowd.com.br/judge/pt/problems/view/1156

def main() -> None:
    soma: float = 1
    a: float = 3
    b: float = 2
    for _ in range(19):
        soma += a / b
        a += 2
        b *= 2

    print(f'{soma:.2f}')

if __name__ == "__main__":
    main()