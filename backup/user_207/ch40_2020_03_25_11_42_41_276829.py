valores = []
i=0
S = 0

def soma_valores(i):
    S =+ valores[i]
    while i < len(valores):
        soma_valores(i)
        i =+1
    return S
    