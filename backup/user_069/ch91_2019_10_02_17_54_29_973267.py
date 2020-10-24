def conta_letras_a (palavra):
    contador = 0
    if palavra[:1] == 'a' or palavra[:1] == 'A':
        contador += 1
        return contador
    
with open('palavras.txt', 'w') as arquivo:
    arquivo.write(conta_letras_a(palavra))
with open('palavras.txt','r') as arquivo:
    conteudo = arquivo.read()