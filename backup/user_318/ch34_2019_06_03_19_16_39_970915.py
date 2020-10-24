deposito=float(input("Qual foi o depósito ?"))
juros=float(input("Qual é a taxa de juros da poupança ?"))

lista=[0]*25
lista[0]=deposito

i=0
while i < 24:
    lista[i+1]=lista[i]*juros
    print(lista[i+1])
    i+=1
print(lista[-1]-lista[0])
          

      