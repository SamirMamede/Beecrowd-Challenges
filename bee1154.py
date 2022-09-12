# https://www.beecrowd.com.br/judge/pt/problems/view/1154

def main() -> None:

    soma = 0
    pessoas = 0
    while True:
        idade = int(input())

        if idade > 0:
            soma += idade
            pessoas += 1
        if idade < 0:
            break
    media = soma / pessoas
    print('{:.2f}'.format(media))


if __name__ == "__main__":
    main()