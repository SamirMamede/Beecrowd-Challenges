# https://www.beecrowd.com.br/judge/pt/problems/view/1114

def main() -> None:

    while True:
        senha = input().strip()
        if senha == '2002':
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')


if __name__ == "__main__":
    main()