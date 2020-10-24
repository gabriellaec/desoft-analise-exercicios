#Recebe uma lista de listas e devolve o valor máximo, Norma N
def encontra_maximo(A):
    #Ganhador da primeira linha
    a = max(A[0])
    b = max(A[1])
    c = max(A[2])
    return max(a,b,c)