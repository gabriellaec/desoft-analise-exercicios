with open('churras.txt', 'r') as arquivo_csv:
    cada_linha = arquivo_csv.readlines()
    i=0
    total=0
    while i < len(cada_linha):
        sem_pular = lista[i].strip()
        novo = sem_pular.split(',')
        total += int(novo[1]) * float(novo[2])
        i+=1
print(total)
    