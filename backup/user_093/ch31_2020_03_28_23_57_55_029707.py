num=int(input("Digite um numero"))
contador=1
primo=True
while contador <= num:
    if num%2==1:
        contador=contador+1
        primo=True
        break
    else:
        primo=false
        break