with open("churras.txt",'r') as arquivo:
    churrasco=arquivo.read()
churrascolista=churrasco.split(',')
contador=0
contador1=1
contador2=2
total=0
while contador<len(churrascolista):
    produto=churrascolista[contador1]*churrascolista[contador2]
    total+=produto
    contador+=0
    contador1+=3
    contador2+=3
print(total)