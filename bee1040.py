n1, n2, n3, n4 = map(float, input().split(" "))

media = (n1*2 + n2*3 + n3*4 + n4)/10

if(media >= 5.0 and media <= 6.9):
    nota_exane = float(input())
    media_final = (nota_exane + media) / 2
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {nota_exane:.1f}")
    if(nota_exane + media /2 >= 5.0):
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
elif(media >= 7.0):
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
