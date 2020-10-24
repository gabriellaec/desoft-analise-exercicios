vi=float(input("qual o depósito inicial? "))
vm=float(input("qual o depósito mensal? "))
J=float(input("qual a taxa de jurus? "))
contador=0
v=vi
while contador<24:
    v=v*(1+J/100)
    print("{0:.2f}".format(v))
    v+=vm
    contador+=1
g=v-vi
print("você ganhou {0:.2f}".format(g))