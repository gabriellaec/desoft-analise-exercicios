with open('dados.csv', 'w') as arquivo:
    arq=arquivo.write()
    x=arq.replace(',', '	')
    with open('dados.tsv', 'w') as file:
    y=file.write(x)
    print(y)
    
    