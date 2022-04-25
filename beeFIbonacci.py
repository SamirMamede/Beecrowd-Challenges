n = int(input())
f = [0, 1]

while len(f) < n:
    f.append(f[-1] + f[-2])

for valor in range(n):
    if valor == n-1:
        print(f[valor], end='\n')
    else:
        print(f[valor], end=' ')
