def eh_primo(n):
    div=3
    if n<2:
        return False
    if n%2==0 and n!=2:
        return False
    while n > div:
        if n%div==0:
            return False
        div +=2
    return True
def verifica_primos(lista):
    dicionario=dict()
    for i in lista:
        if eh_primo(i)==True:
            dicionario[i]="True"
        else:
            dicionario[i]="False"
    return dicionario
    
    