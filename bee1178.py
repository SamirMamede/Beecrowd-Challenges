# https://www.beecrowd.com.br/judge/pt/problems/view/1178

def main() -> None:
    numero = float(input())
    lista = [numero]
    for i in range(1, 100):
        lista.append(lista[i - 1] / 2)

    for index, valor in enumerate(lista):
        print(f'N[{index}] = {valor:.4f}')


if __name__ == "__main__":
    main()