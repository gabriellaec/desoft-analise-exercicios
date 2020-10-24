def classifica_idade (idade)
idade= int(input("Qual a sua idade"))
if idade <=  11:
     print("crianca")
elif idade >= 12 or idade <= 17 :
     print("adolescente")
else:
    print("adulto")