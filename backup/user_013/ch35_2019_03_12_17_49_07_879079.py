#Depósitio inicial (i)
i = float(input())
#Depósito mensal (m)
m = float(input())
#Taxa de juros (j)
j = float(input())
# Número de mês (n)
n = 2
#Extrato (E)
E = i*(1+j)
print (round(E,2))
while n < 24:
    E = ((E)*(1+j))+m
    print(round(E,2)) 
    n = n + 1
    
print(round(E-i,2))