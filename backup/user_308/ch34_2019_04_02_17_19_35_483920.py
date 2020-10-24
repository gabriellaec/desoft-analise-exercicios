dep=float(input("Qual é o depósito inicial?: "))
taxa=float(input("Qual é a taxa de juros por mês?: "))
tf=1+taxa
i=0
ganho=0
valor_antigo=dep
while i<=24:
    valor=valor_antigo*tf
    print ("Valor do mês {0}: {1}".format(i,valor))
    ganho+=valor-valor_antigo
    i+=1
    valor_antigo=valor
print(ganho)