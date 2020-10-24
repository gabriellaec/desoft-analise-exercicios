def remove_vogais(x):
    z=list(x)
    nl=[]
    for v in range(0,len(z)):
        if (z[v]!="a") and  (z[v]!="e") and (z[v]!="i") and (z[v]!="o") and (z[v]!="u"):
            nl.append(z[v])  
    volta_p_string="".join(nl)           
    return volta_p_string