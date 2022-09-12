# https://www.beecrowd.com.br/judge/pt/problems/view/1149 

def main() -> None:

    ler = input().split()
    inicial, final, *resto = [int(num) for num in ler]

    if final <= 0:
        for numero in resto:
            final = numero
            if final > 0:
                break
    soma = 0

    itens = [i for i in range(final)]

    for item in itens:
        soma += inicial + item

    print(soma)


if __name__ == "__main__":
    main()