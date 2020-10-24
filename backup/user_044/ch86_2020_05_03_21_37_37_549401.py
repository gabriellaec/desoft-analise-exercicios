with open('dados.csv', 'r') as arquivo:
    arq=arquivo.read()
    x=arq.replace(',', "\t")
    with open('dados.tsv', 'a+') as file:
        y=file.write(x)