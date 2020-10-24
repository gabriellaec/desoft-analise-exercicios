def acha_bigramas(string):
    lista = []
    for i in range(len(string)):
        bigrama = string[i]+string[i+1]