with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
    a.replace(',', '\t')
    print(a)
