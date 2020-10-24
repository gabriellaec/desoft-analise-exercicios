def conta_letras(palavra)
    dic={}
    for letra in palavra:
        dic[letra] = palavra.count(letra)
return dic