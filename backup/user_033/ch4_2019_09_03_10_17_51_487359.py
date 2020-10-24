def classifica_idade(idade)

x = input("declare a idade da pessoa\n")

if idade <= 11:
    print("crianca")
elif idade >=12 and idade <=17:
    print("adolescente")
else: print("adulto")

y = classifica_idade
y(x)