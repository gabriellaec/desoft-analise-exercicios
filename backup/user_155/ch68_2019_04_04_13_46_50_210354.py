alunos = ['a','b','c','d','e','f','g']
def separa_trios(alunos):
    i = 0
    j = i + 1
    t = 3*i
    w = 3*j
    lista = []
    while i < len(alunos)/3:
        trio = alunos[t:w]
        lista.append(trio)
        i = i + 1
        j = i + 1
        t = 3*i
        w = 3*j
    return lista
   
    	
print(separa_trios(alunos))       