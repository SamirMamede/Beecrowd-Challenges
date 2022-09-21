# https://www.beecrowd.com.br/judge/pt/problems/view/1828

def win(a, b):
    if a == 'tesoura' and b == 'papel':
        return 1
    elif a == 'papel' and b == 'tesoura':
        return 2
    elif a == 'papel' and b == 'pedra':
        return 1
    elif a == 'pedra' and b == 'papel':
        return 2
    elif a == 'pedra' and b == 'lagarto':
        return 1
    elif a == 'lagarto' and b == 'pedra':
        return 2
    elif a == 'lagarto' and b == 'Spock':
        return 1
    elif a == 'Spock' and b == 'lagarto':
        return 2
    elif a == 'Spock' and b == 'tesoura':
        return 1
    elif a == 'tesoura' and b == 'Spock':
        return 2
    elif a == 'tesoura' and b == 'lagarto':
        return 1
    elif a == 'lagarto' and b == 'tesoura':
        return 2
    elif a == 'lagarto' and b == 'papel':
        return 1
    elif a == 'papel' and b == 'lagarto':
        return 2
    elif a == 'papel' and b == 'Spock':
        return 1
    elif a == 'Spock' and b == 'papel':
        return 2
    elif a == 'Spock' and b == 'pedra':
        return 1
    elif a == 'pedra' and b == 'Spock':
        return 2
    elif a == 'pedra' and b == 'tesoura':
        return 1
    elif a == 'tesoura' and b == 'pedra':
        return 2
    else:
        return 3


def main() -> None:

    casos = int(input())

    for i in range(1, casos + 1):
        sheldon, raj = input().strip().split()

        reacao = win(sheldon, raj)
        if reacao == 1:
            reacao = 'Bazinga!'
        elif reacao == 2:
            reacao = 'Raj trapaceou!'
        elif reacao == 3:
            reacao = 'De novo!'

        print(f'Caso #{i}: {reacao}')


if __name__ == "__main__":
    main()