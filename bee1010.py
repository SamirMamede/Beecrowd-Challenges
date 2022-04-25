linha1 = input('').split()
linha2 = input('').split()
a, b, c = linha1
d, e, f = linha2
valor_a_pagar = int(b) * float(c) + int(e) * float(f)
print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')
