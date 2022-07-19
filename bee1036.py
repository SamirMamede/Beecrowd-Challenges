import math

try:
    a, b, c = map(float, input().split(" "))

    delta = b * b - 4 * a * c
    delta = math.sqrt(delta)

    r1 = (-b + delta) / (2 * a)
    r2 = (-b - delta) / (2 * a)

    print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
except:
    print("Impossivel calcular")