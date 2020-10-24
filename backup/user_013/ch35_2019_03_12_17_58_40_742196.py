#Depósitio inicial (i)
i = float(input())
#Depósito mensal (m)
m = float(input())
#Taxa de juros (j)
j = float(input())
# Número de mês (n)
n = 2
#Extrato do mês 1(E)
E = i
print (round(E,2))
while n < 25:
    #Extrato do mês n
    E = ((E)*(1+j))+m
    print(round(E,2)) 
    n = n + 1
    
print(round((E-(i+m*23)),2))