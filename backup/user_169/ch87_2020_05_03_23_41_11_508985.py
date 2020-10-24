with open('churras.txt','r') as arquivo:
    
    a=arquivo.read()
    
    b=a.split(',')
    
    lista=[]
    i=1
    e=2
    
    while i < len(b) and e< len(b):
        lista.append(float(b[i])*float(b[e]))
        i+=3
        e+=3
    
    print(sum(lista))
    
    