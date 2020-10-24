
def alunos_impares(x):
    x=0
    for i in alunos:
        x+=1
        if x%2 !=0 :
            alunos2.append(i)
    return alunos2
    print(alunos2)