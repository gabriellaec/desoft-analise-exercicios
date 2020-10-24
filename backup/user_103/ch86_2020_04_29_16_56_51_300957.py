with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
    a.replace(',', '/')
    print(a)
