with open('dados.csv', 'r') as arquivo:
    arq=arquivo.write()
    x=arq.replace(',', "\t")
    with open('dados.tsv', 'a+') as file:
    y=file.write(x)
    print(y)
    
    