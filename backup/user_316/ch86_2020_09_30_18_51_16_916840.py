with open('dados.csv', 'r') as file:
    content = file.read()
    
with open('dados.csv', 'x') as file:
    file.write(content.replace(',', '	'))
    