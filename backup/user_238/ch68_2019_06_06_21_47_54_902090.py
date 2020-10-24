def separa_trios(alunos):
    lista=[]
    if len(alunos)>0:
        while len(alunos)>=3:
            lista.append(alunos[:3])
            del alunos[:3]
            
        lista.append(alunos)
    else:
        return " "
    return lista

alunos=[]
print(separa_trios(alunos))