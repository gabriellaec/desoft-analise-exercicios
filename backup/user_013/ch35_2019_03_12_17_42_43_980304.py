#Depósitio inicial (i)
i = int(input())
#Depósito mensal (m)
m = int(input())
#Taxa de juros (j)
j = float(input())
# Número de mês (n)
n = 2
#Extrato (E)
E = i
print (E)
while n < 24:
    E = (E)*(1+j)+m
    print(E) 
    n = n + 1
    
print(E-i)