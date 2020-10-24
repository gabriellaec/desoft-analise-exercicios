with open('dados.csv', 'r') as arquivo:
    texto = arquivo.read()
    text = texto.replace(",","	")
    
with open('churras.tsv', 'w') as arquivo:
    arquivo.write(text)print(text)