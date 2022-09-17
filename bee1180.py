# https://www.beecrowd.com.br/judge/pt/problems/view/1180

def main() -> None:
    input()
    valores = [int(numero) for numero in input().strip().split()]

    menor = min(valores)

    print(f'Menor valor: {menor}')
    print(f'Posicao: {valores.index(menor)}')


if __name__ == "__main__":
    main()