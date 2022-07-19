idade_dias = int(input())

ano = idade_dias//365

mes = idade_dias%365
mes = mes//30

dias = idade_dias%365
dias = dias%30

print(f"{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)")