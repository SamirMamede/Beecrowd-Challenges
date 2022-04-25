while True:
    num = list(map(int, input().split()))
    tamanholista = len(num)
    if tamanholista > 3:
        continue
    elif tamanholista < 3:
        continue
    else:
        print(f'{max(num)} eh o maior')
        break