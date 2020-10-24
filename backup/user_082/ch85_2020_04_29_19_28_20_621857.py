with open('macacos-me-mordam.txt', 'r') as arquivo:
    estoque_bananas = arquivo.read()
    banana_lowercase = estoque_bananas.lower()
    j=0
    for i in len(banana_lowercase):
        if i == 'banana':
            j+=1
        else: 
            continue
        
    print(j)
            