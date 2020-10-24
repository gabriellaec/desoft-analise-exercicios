def verifica_progressao(num):
    pg=True 
    pa=True
    ag=True
    i=0
    
    while i<(len(num)-2) and pg==True:
        if num[i+2]/num[i+1]==num[i+1]/num[i]:
            pg=True
        else:
            pg=False
        i=i+1
        
    while i<(len(num)-2) and pa==True:
        if num[i+2]-num[i+1]==num[i+1]-num[i]:
            pa=True
        else:
            pa=False
        i=i+1     
        
    if pg==True and pa==False:
        return "PG"
    elif pa==True and pg==False:
        return "PA""
    elif pa==True and pg==False:
        return "AG""    
    else:
        return "NA"
        