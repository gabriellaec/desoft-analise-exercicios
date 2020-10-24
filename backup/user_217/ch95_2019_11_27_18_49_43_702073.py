def mais_populoso(brasil):
    for a in brasil:
        lista=[]
        s = 0
        for b in brasil[a]:           
            s += brasil[a][b]
        lista.append(s)

     estados = {"São Paulo":s[0],
               "Minas Gerais":s[1]}
     
     for k,v in estados.items():