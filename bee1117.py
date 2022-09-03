# https://www.beecrowd.com.br/judge/pt/problems/view/1117

def main() -> None:

    validas = 0
    soma: float = 0.0
    while True:
        if validas == 2:
            break
        nota = float(input())
        if 0 <= nota <= 10:
            validas += 1
            soma += nota
        else:
            print('nota invalida')
    media: float = soma / 2
    print('media = {}' .format(media))


if __name__ == "__main__":
    main()