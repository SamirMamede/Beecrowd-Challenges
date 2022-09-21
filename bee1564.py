# https://www.beecrowd.com.br/judge/pt/problems/view/1564

def main() -> None:
    while True:
        try:
            r = int(input())
            if r == 0:
                print('vai ter copa!')
            elif r > 0:
                print('vai ter duas!')
        except EOFError:
            break


if __name__ == "__main__":
    main()