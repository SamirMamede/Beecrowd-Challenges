# https://www.beecrowd.com.br/judge/pt/problems/view/1142

def main() -> None:

    x = 1
    y = 2
    z = 3
    n = int(input())

    for i in range(n):
        print(f'{x} {y} {z} PUM')
        x += 4
        y += 4
        z += 4


if __name__ == "__main__":
    main()