#valores = input('').split()
#A, B, C = valores
#area_triangulo = (float(A) * float(C)) / 2
#area_circulo = 3.14159 * float(C)**2
#area_trapezio = ((float(A) + float(B)) * float(C)) / 2
#area_quadrado = float(B)**2
#area_retangulo = float(A) * float(B)
#print(f'TRIANGULO: {area_triangulo:.3f}')
#print(f'CIRCULO: {area_circulo:.3f}')
#print(f'TRAPEZIO: {area_trapezio:.3f}')
#print(f'QUADRADO: {area_quadrado:.3f}')
#print(f'RETANGULO: {area_retangulo:.3f}')


valor = list(map(lambda x: float(x), input().split()))
A, B, C = valor[0], valor[1], valor[2]
area_triangulo = (A * C) / 2
area_circulo = 3.14159 * C**2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B**2
area_retangulo = A * B
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
