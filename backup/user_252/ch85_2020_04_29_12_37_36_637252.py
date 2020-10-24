with open('macacos-me-mordam.txt', 'r') as arquivo:
    macaco=arquivo.read().split()
k=0
for i in macaco:
    palavra=i.lower()
    if palavra == 'banana':
        k+=1
print(k)
    

    
