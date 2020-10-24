def classifica_idade (X):
    y = X
    return y
idade = 15
idade2 = classifica_idade(idade)
if idade2 <= 11:
    print("crianca")
elif idade2 >= 12 and idade2 <=17:
    print("adolescente")
else:
    print("adulto")