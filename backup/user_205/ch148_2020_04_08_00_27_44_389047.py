def conta_letras(string): 
    dic={}
    for caractere in string:
        dic[caractere]=string.count(caractere)
    return dic