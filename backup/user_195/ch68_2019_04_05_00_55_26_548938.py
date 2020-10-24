def separa_trios(L):
    alunos=len(L)
    i=0
    S=[]
    if alunos%3==0:
        while i<alunos:
            S.append(L[i:i+3])
            i+=3
    elif alunos%3==2:
        while i<alunos-2:
            S.append(L[i:i+3])
            i+=3
        S.append(L[alunos-2:alunos])
    else:
        while i<alunos-1:
            S.append(L[i:i+3])
            i+=3
        S.append(L[alunos-1:alunos])
    return S