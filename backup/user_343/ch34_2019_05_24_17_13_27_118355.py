
d=int(input("Qual é o valor?"))
tx=float(input("Taxa?"))
valores=[d]
i=0

while i<=24:
    valores.append(valores[i]*tx)
    print(valores[i])
    i+=1
print(valores[24]-valores[0])
    

                          