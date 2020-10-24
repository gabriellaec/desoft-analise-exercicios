# Guarda conteudo do arquivo em uma string
with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    novo_conteudo = conteudo.replace(',', '\t')

# Reescreve com o conteúdo salvo substituindo os caracteres
with open('dados.csv', 'w') as dados:
    dados.write(novo_conteudo)