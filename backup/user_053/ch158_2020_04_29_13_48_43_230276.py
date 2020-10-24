with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    # Remove espaços
    frase = conteudo.strip()
    # Conta palavras
    lista = frase.split()
    numero = len(lista)

print(numero)