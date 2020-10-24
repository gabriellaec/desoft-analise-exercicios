
def separa_trios(alunos):
    lista=[]
    while len(alunos)>=3:
        lista.append(alunos[:3])
        del alunos[:3]
        
    lista.append(alunos)
    return lista

alunos=['a','b','c','d']
print(separa_trios(alunos))