def verifica_progressao (numeros):
    conpa=0
    c=[]
    for i in range (len(numeros)-1):
        c.append (numeros[i+1]-numeros[i])
        if len (c)>1:
            if c[i]==c[i-1]:
                conpa=conpa+1
    if conpa==len(c)-1:
        pa=True
    else:
        pa=False


    conpg=0
    g=[]
    for i in range (len(numeros)-1):
        g.append (numeros[i+1]/numeros[i])
        if len (g)>1:
            if g[i]==g[i-1]:
                conpg=conpg+1

    if conpg==len(g)-1:
        pg=True
    else:
        pg=False
    
    
    if len(numeros)==2:
        return "Na"
    elif pa==True and pg==False:
        return "PA"
    elif pa==False and pg==True:
        return "PG"
    elif pa==True and pg==True:
        return "AG"
    elif pa==False and pg==False:
        return "Na"
    elif len(numeros)==2:
        return "Na"