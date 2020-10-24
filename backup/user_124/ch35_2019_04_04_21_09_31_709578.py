dep_inicial = int(input("qual o deposito inicial? : "))
dep_mensal = int(input("qual o deposito mensal? : "))
taxa = int(input("qual a taxa de juros? : "))

montante = dep_inicial * (1 + taxa)
print("para o mes 1 o montante é igual a : {0:.2f}".format(montante))

tempo = 1
while tempo <= 24:
    montante = (dep_inicial + dep_mensal * tempo) * (1 + taxa) ** (tempo + 1)
    print("o valor do montante para o {0} mes é {1:.2f}".format(taxa , montante))
    tempo +=1
J = montante - dep_inicial - 24 * dep_mensal
print("{0:.2f}".format(J))
