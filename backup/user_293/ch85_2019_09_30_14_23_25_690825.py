with open("macacos-me-mordam.txt","r") as variavel:
    arquivo = variavel.read()
    arquivo = arquivo.lower()
    arquivo = arquivo.split()
i = 0
for n in arquivo:
    if n == "banana":
        i += 1
print(i)
    
    
