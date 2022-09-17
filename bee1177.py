# https://www.beecrowd.com.br/judge/pt/problems/view/1177

def main() -> None:

    numero = int(input())

    for i in range(1000):
        print(f'N[{i}] = {i % numero}')


if __name__ == "__main__":
    main()