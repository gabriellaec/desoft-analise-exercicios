numeros=[]
n=int(input("Digite um numero: "))
while(n>0):
    numeros.append(n)
    n=int(input("Digite um numero: "))
i=0
quant=len(numeros)
while(quant>i):
    print(numeros[quant-1])
    quant-=1
         
  