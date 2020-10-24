def estritamente_cresente(a):
    if a:
        pedro=[a[0]]
        i=1
        while i<len(a):
            x=a[i]
            if x>pedro[-1]:
                pedro.append(x)
            i+=1
        return pedro
    else:
        return[]
            
            
      