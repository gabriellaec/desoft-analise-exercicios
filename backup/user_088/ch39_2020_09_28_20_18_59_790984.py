numero=int(input('Qual o numero gera a maior sequencia'))
n=0
while(numero<1000 and numero>0):
                 if(numero%2==0):
                     numero*=1/2
                 elif(numero%2!=0):
                    numero=3*numero+1
            n+=1
print(numero)