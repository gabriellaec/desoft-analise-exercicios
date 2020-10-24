with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
    a.split()
    lista=[]
    i=0
    while i < len(a):
        if a[i]!=',':
            lista.append(a[i])
            i+=1
        else:
            i+=1
    '	'.join(lista)
        print(lista)
