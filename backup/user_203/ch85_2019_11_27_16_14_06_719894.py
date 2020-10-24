i = 0
with open ('macacos-me-mordam.txt','r') as arquivo:
    for line in arquivo:
        for palavras in line.split():
            if palavras.lower() == 'banana':
                i += 1 
print (i) 
    