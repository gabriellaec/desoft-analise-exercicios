
d=float(input("Qual é o valor?"))
tx=float(input("Taxa?"))/100
valores=[d]
i=1

while i<=24:
    valores.append(valores[i-1]*tx)
    print("{0:.2f}".format(valores[i]))
    i+=1
print("{0:.2f}".format(valores[24]-valores[0]))
    

                          