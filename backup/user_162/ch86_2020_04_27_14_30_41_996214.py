with open('dados.csv', 'r') as arquivo:
    texto = arquivo.read()
    text = texto.replace(",","	")
    
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(text)