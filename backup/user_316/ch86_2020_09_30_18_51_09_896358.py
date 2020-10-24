with open('dados.csv', 'r') as file:
    content = file.read()
    
with open('dados.tsv', 'x') as file:
    file.write(content.replace(',', '\t'))
    