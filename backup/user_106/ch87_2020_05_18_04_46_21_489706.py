with open ('churras.txt', 'r') as arq:
    listao=arq.readlines()
i=0
total=0
while i<len(listao):
    sem_pular=listao[i].strip()
    novo=sem_pular.split(',')
    total+=novo[1]*novo[2]
    i+=1
print (total)