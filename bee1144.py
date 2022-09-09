# https://www.beecrowd.com.br/judge/pt/problems/view/1144

def main() -> None:

    n = int(input())
    n *= 2
    x = y = z = 1

    for i in range(1, n + 1):
        if i % 2 == 1 and i != 1:
            y += i - 1
            x += 1
            z = x * y

        if i % 2 == 0:
            y += 1
            z += 1

        print(x, y, z)


if __name__ == "__main__":
    main()