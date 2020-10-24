deposito=float(input("Qual foi o depósito ?"))
juros=float(input("Qual é a taxa de juros da poupança ?"))
lista_valores=[]
lista_valores[0]=deposito
i=0
while i < 24:
    lista_valores[i+1]=lista_valores[i]*juros
    print(lista_valores[i+1])
    i+=1
print(lista-valores[-1]-lista_valores[0])
          

      