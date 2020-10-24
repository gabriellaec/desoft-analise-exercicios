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
    
    while i<len(dvalue):
        z[dkey[i]]=dvalue[i]
        if z[dkey[i]]==z[dkey[i]]:
            z[dkey[i]]=dvalue[i],dvalue[i-2]
            
        i+=1
          
    return (z)