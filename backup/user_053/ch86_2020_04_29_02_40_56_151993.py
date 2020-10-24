# Guarda conteudo do arquivo em uma string
with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()

# Reescreve com o conteúdo salvo substituindo os caracteres
with open('dados.csv', 'w') as dados:
    novo_conteudo = conteudo.replace(',', '\t')
    dados.write(novo_conteudo)