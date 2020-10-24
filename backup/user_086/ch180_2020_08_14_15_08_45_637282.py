def ocorrencias_letras(s):
    dic = {}
    i = 0
    while i < len(s):
        letra = s[i]
        if letra in dic:
            x = dic[letra]
            x+=1
            dic[letra] = x
        else:
            dic[letra] = 1
        i+=1
        
    return dic