def estritamnete_crescente (l):        
 
    if len(l)>0:
  
        r=[l[0]]
        i=1

        while i<len(l):
        
            if(l[i]>r[len(r)-1]):  #pegando sempre o último elemento do r
                r.append(l[i])   
            i+=1 
  
        return r
  
    else:
        
        return []
