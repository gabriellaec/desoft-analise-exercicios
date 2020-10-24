par = 0
impar = 0
def verifica_lista(lista):
    for numeros in lista:
        if numeros%2 == 0:
            par+=1
        elif numero%2 !=0:
            impar+=1
    if impar >0 and par ==0:
        return "ímpar"
    elif impar==0 and par>0:
        return "par"
    else: 
        return "misturado"
        