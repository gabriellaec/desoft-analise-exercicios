#Depósitio inicial (i)
i = float(input())
#Depósito mensal (m)
m = float(input())
#Taxa de juros (j)
j = float(input())
# Número de mês (n)
n = 1
#Extrato do mês 1(E)
#E = i
print ('{:.2f}'.format(E))
while n < 25:
    #Extrato do mês n
    E = E*(j+1)+m
    print ('{:.2f}'.format(E))
    n = n + 1    
print('{:.2f}'.format(E - (i + m*24)))