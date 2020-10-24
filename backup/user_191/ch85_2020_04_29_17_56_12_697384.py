with open('macacos-me-mordam.txt','r') as arquivo:
    arquivo.lower()
    x=[]
    x.append(arquivo.find("banana"))
    print(len(x))