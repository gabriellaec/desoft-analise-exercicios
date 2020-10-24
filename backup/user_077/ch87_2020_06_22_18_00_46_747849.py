with open ('churras.txt', 'r') as arquivo:
    lista=arquivo.readlines()
i=0
total=0
while i<len(lista):
    recortado=lista[i].strip()
    separado=srecortado.split(',')
    total+=int(separado[1])*float(separado[2])
    i+=1
print (total)