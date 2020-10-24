with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
    a.split()
    a.replace(',', '\t')
    print(a)
