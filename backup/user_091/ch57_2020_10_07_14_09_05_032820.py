def verifica_progressao(lista):
    if lista=[] or len(lista)==1:
        return 'NA'
    elif len(lista)==2:
        return 'AG'
    else:
        pa=True
        pg=True
        i=0
        while i<len(lista):
            if not lista[i]+lista[i-2]==2*lista[i-1]:
                pa=False
            if not lista[i]*lista[i-2]==(lista[i-1])**2:
                pg=False
            i+=1
        
        if pa=True and pg=False:
            return 'PA'
        elif pa=False and pg=False:
            return 'NA'
        elif pa=False and pg=True:
            return 'PG'
        elif pa=True and pg=True:
            return 'AG'
