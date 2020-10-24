def lots_of_bananas():
    
   
    banana_list=[]
    up_list=[]
    contador=0 
    
    with open("macacos-me-mordam.txt", 'r') as file1:
        
        
        for b in file1:
            banana_list.append(b)
        
        for banana in banana_list:
            up_list.append(banana.upper())
        print(up_list)

        for a in up_list:
            j = a.split(",")
            
            
            for k in j:
                k=k.split(' ')
                print(k)
                for c3 in k:
                
                    if c3 == "BANANA":
                        contador+=1
        
            
        
    
            
         
    return contador

print(lots_of_bananas())
    
    
    