dep=float(input('Qual o depósito inicial?'))
dep_mensal=float(input('Qual o depósito mensal?'))
taxa_juros=float(input('Qual a taxa de juros?'))
dep_inicial=dep
m=0
while m<=24:
    if m==0:
        dep=dep
    else:
        dep=dep*(1+taxa_juros)+dep_mensal
    print('No mês {0}, o saldo é de {1:.2f}'.format(m,dep))
    m+=1
print('O ganho total foi de {0:.2f}'.format(dep-dep_inicial))

