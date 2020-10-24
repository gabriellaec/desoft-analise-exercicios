with open("churras.txt",'r') as arquivo:
    tx=arquivo.read()
    
lista=tx.split(",")
b=lista[1::3]
a=lista[2::5]
i=0
valor=0
while i<len(a):
    valor+=a[i]*b[i]
    i+=1
print(valor)
