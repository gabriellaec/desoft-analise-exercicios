
d=int(input("Qual é o valor?"))
tx=float(input("Taxa?"))
valores=[d]
i=0

while i<23:
    valores.append(valores[i]*tx)
    i+=1
print(valores[23]-d)

                          