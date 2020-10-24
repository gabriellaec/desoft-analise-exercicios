def conta_letras(string):
    dic={}
    for letras in string:
        if letras not in dic.keys():
            dic[letras]=string.count(letras)
    return dic