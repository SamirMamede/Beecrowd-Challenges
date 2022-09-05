# https://www.beecrowd.com.br/judge/pt/problems/view/1131

def main() -> None:

    interwins = 0
    gremiowins = 0
    empates = 0
    grenais = 1

    while True:
        gols = input().strip().split()

        inter = int(gols[0])
        gremio = int(gols[1])

        if inter > gremio:
            interwins += 1
        if gremio > inter:
            gremiowins += 1
        if gremio == inter:
            empates += 1

        resposta = 0
        while resposta != 1 and resposta != 2:
            print('Novo grenal (1-sim 2-nao)')
            resposta = int(input())
        if resposta == 2:
            break

        grenais += 1
        inter = gremio = 0
    print(f'{grenais} grenais')
    print(f'Inter:{interwins}')
    print(f'Gremio:{gremiowins}')
    print(f'Empates:{empates}')
    if gremiowins > interwins:
        print('Gremio venceu mais')
    elif interwins > gremiowins:
        print('Inter venceu mais')
    else:
        print('Nao houve vencedor')


if __name__ == "__main__":
    main()