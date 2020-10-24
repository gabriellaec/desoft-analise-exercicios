#Escreva o programa do depósito inicial d
d = float(input())
#Taxa de juros j
j = float(input())
#Lista de dos valores V
V = [0]*24
#Contador 
i = 1
#Primeiro mês
V[0] = d*(1+j)
#Looping
while i < len(V):
    V[i] = V[i-1]*(1+j)
    i += 1
for k in range(0,23):
    print(V[k])