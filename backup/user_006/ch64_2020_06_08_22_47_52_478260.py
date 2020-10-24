def acha_bigramas(palavra):
    listabi=[]
    i=0
    while i<(len(palavras)-1):
        bi=palavra[i]+palavra[i+1]
        listabi.append(bi)
        i=i+1
    return listabi