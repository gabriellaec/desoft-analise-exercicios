lista_usuario = []
palavra = input('Digite uma palavra: ')
# Cria lista de palavras do usuário
while palavra != 'fim':
    lista_usuario.append(palavra)
    palavra = input('Digite uma palavra: ')

# Verifica iniciais
for palavra in lista_usuario:
    if palavra[0] == 'a':
        print(palavra)