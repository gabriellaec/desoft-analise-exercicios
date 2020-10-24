
def verifica_primos(lista):
    dicionario=dict()
    div=3
    for i in lista:
        if lista[i]%2==0 and lista[i]!=2 or lista[i]==1 or lista[i]==0:
            dicionario[lista[i]]="False"
        while lista[i] > div:
            if lista[i]%div==0:
                dicionario[lista[i]]="False"
            div +=2
        dicionario[lista[i]]="True"
    return dicionario
    
    