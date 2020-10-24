with open('dados.csv', 'r') as arquivo:
    texto = arquivo.read()
    text = texto.replace(",","\t")
    
print(text)