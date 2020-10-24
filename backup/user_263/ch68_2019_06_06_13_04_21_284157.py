def separa_trios(alunos):
    trios=[]
    lista_de_um = []
    i=0
    if len(alunos)%3==0:
        while i<len(alunos):
            trios.append(alunos[i:i+3])
            i+=3
    elif len(alunos)%3==2:
        while i<(len(alunos)-2):
            trios.append(alunos[i:i+3])
            i+=3
        trios.append(alunos[(len(alunos)-2):len(alunos)])
    elif len(alunos)%3==1:
        while i<(len(alunos)-1):
            trios.append(alunos[i:i+3])
            i+=3
        lista_de_um.append(alunos[len(alunos)-1])
        trios.append(lista_de_um)
    return trios 

alunos = ['andre']
print(separa_trios(alunos))