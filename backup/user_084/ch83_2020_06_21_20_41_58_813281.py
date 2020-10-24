def medias_por_inicial(nomes):
    media1={}
    media2={}
    for a,n in nomes.Items():
        if a[0] in media1:
            media1[a[0]][0]+=n
            media1[a[0]][1]+=1
        else:
            media1[a[0]]=[n, 1]
    for inicial,media in media1.Items:
        media2[inicial]=media1[0]/media1[1]
    return media2
    
            
                       
        
        
        
            

         
            
            
    