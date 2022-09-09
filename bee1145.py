# https://www.beecrowd.com.br/judge/pt/problems/view/1145

def main() -> None:

    valores = input().split()
    x, y = [int(num) for num in valores]

    i = 1
    while i <= y:
        if i % x == 0:
            print(f'{i}')
        else:
            print(f'{i} ', end='')
        i += 1


if __name__ == "__main__":
    main()