# https://www.beecrowd.com.br/judge/pt/problems/view/1118

def main() -> None:

    validas: int = 0
    soma: float = 0
    while True:
        if validas == 2:
            media = soma / 2
            print('media = {:.2f}' .format(media))
            validas = soma = media = 0
            resposta = 0
            while resposta not in {1, 2}:
                print('novo calculo (1-sim 2-nao)')
                resposta = int(input())
            if resposta == 2:
                break
        nota = float(input())
        if 0 <= nota <= 10:
            validas += 1
            soma += nota
        else:
            print('nota invalida')


if __name__ == "__main__":
    main()