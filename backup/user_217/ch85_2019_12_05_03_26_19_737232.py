with open('macacos-me-mordam.txt','r') as conteudo:
    contador=0
    for l_num, l in enumerate(conteudo, 1):
        if 'Banana' in l:
            contador+=1
        
        if 'BANANA'  in l:
            contador+=1
        
        if 'BaNaNa'  in l:
            contador+=1
		if 'banana'  in l:
            contador+=1
        if 'bAnAnA' in l:
            contador+=1
        if 'BAnAnA' in l:
            contador+=1
            
conteudo.close()       
print(contador)