lista_palavras = []

palavra = input('Palavra? ')

while palavra != 'fim' :
    lista_palavras.append(palavra)
    palavra = input('Outra palavra?')

i = 0
while i < len(lista_palavras):
    palavra_colocada_pelo_usuário = lista_palavras[i]
    if len(palavra_colocada_pelo_usuário) > 1 and palavra_colocada_pelo_usuário[0] == 'a' :
        print(palavra_colocada_pelo_usuário)
    i += 1