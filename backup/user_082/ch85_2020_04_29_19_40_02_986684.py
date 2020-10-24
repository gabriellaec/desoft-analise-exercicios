with open('macacos-me-mordam.txt', 'r') as arquivo:

    arquivo_read = arquivo.read()
    banana_list = arquivo_read.split()
    j=0
    
    for i in banana_list:
        
        banana_lower = i.lower()
        
        if banana_lower == 'banana':
            j+=1
            
        else: 
            j+=0
            
print(j)
            