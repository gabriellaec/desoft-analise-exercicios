contador=0
vinicial=float(input(qual o valor inicial))
J=float(input(qual o valor do juros))
v=vinicial
while contador<24:
    contador+=1
    v=v*(1+J/100)
    print ("você terá {0:.2f} no mes {1}".format(v,contador)
ganho=v-vinicial
print("você ganhou{0:.2f}".format(ganho))