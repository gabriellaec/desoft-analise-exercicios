dep=int(input('Qual o deposito inicial? ')
juros=int(input('Qual a taxa de juros da poupanca? ')
m=1
l=0
while m<25:
    l=dep+dep*juros**m
    m+=1
    return l
print (dep*juros**m)          