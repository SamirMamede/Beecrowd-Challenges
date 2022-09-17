# https://www.beecrowd.com.br/judge/pt/problems/view/1181

def main() -> None:
    tamanho_da_matriz = 12
    soma: float = 0

    line = int(input())
    op = input().upper().strip()  # SOMA OU MEDIA
    matriz: list[list[float]] = [[float(input()) for _ in range(
        tamanho_da_matriz)] for _ in range(tamanho_da_matriz)]

    for celula in matriz[line]:
        soma += celula

    if op == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / tamanho_da_matriz))


if __name__ == "__main__":
    main()