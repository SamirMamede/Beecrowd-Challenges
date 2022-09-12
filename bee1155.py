# https://www.beecrowd.com.br/judge/pt/problems/view/1155

def main() -> None:
    soma: float = 0
    for i in range(1, 101):
        soma += 1 / i
    print(f'{soma:.2f}')

if __name__ == "__main__":
    main()
