def numero_digitos(S):
    cont=0
    L= [char for char in S]
    for i in range(len(L)):
        if L[i].isdigit() == True:
            cont+=1
    return cont