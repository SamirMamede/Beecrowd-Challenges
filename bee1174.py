# https://www.beecrowd.com.br/judge/pt/problems/view/1174

def main() -> None:
    vetor: list[float] = [0.0 for _ in range(100)]

    for i in range(100):
        numero = float(input())
        vetor[i] = numero
    for indice, valor in enumerate(vetor):
        if valor <= 10:
            print(f'A[{indice}] = {valor}')


if __name__ == "__main__":
    main()