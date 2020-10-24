alunos = ['a','b','c','d','e','f','g']
def separa_trios(alunos):
    i = 0
    j = i + 1
    lista = []
    while i < len(alunos)/3:
        trio = alunos[i*3:(j*3)]
        lista.append(trio)
        i+=1
    return lista
            
            
        
    