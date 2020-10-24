def conta_letras(palavra):
    dicio={}
    for i in palavra:
        n=0
        for e in palavra:
            if i==e:
                n=n+1
        dicio[i]=n
    return dicio            
                