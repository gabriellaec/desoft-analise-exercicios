sequencia =[]
numero_de_termos =[]
i = 1 #contador  
while i<= 1000:
    x = i
    sequencia.append (x)
    while x != 1:
        if x%2 ==0:
            x = x/2
            sequencia.append(x)
        else:
            x = 3*x + 1
            sequencia.append (x)
    numero_de_termos.append(len(sequencia))
    sequencia = []
    i += 1

print (numero_de_termos)
print (max(numero_de_termos))

j=0
while numero_de_termos[j] < max(numero_de_termos):
       j +=1
print (j +1)