with open('macacos-me-mordam.txt', 'r') as arquivo:
    arquivo_read = arquivo.read()
    banana_list = arquivo_read.split()
    j=0
    for i in banana_list:
        i.lower()
        if i == 'banana':
            j+=1
        else: 
            continue
        
    print(j)
            