def separa_trios(n):
    l=[]
    i=0
    t=0
    while i<len(n):
        l[t].append(n[i,i+3])
        i+=3
        t+=1
    return l
        
  
    