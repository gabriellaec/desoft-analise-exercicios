with open ('churras.txt', 'r') as arq:
    listao=arq.readlines()
i=1
total=0
while i<len(listao)-1:
    total+=int(listao[i])*float(listao[i+1])
    i+=3
print (total)