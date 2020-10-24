def Soma(N):
    texto=str(N)
    soma=0
    for i in range(len(texto)):
        soma+=int(texto[i:i+1])**int(texto[i:i+1])
    return soma
def verifica_numero(N):
    if Soma(N)==N:
        resultado=True
    else:
        resultado=False
    return resultado