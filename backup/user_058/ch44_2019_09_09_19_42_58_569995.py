numero=[]
def soma_valores(numero):
    soma=0
    i=0
    while i<len(numero):
        soma= numero[i]+soma
        i+=1
    return soma
print(soma_valores(numero))