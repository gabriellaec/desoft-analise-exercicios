dic=["janeiro":1,"fevereiro":2]
pergunta=input("Qual o mes?")

for mes, dia in dic.items():
    if pergunta == mes:
    print(dia)