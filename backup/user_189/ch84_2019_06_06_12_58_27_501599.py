def inverte_dicionario(h):
    dk=dict.keys(h)
    dv=dict.values(h)
    dkey=[]
    dvalue=[]
    
    for a in dk:
       	dvalue.append(a)
           
    for b in dv:
       	dkey.append(b)
           
    
    z={}
    i=0
    
    while i<len(dvalue+1):
        dvalue[i]=dict.values(z)
        dkey[i]=dict.key(z)
        i+=1
          
    return (z)
