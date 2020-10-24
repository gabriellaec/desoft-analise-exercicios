#Preenche lista até o usuario digitar 'fim'
lista_palavra=[]
#Define uma variável com a resposta do usuário
palavra=input('Digite uma palavra:')
#Enquanto o usuário não digita 'fim', o loop continua
while palavra != 'fim':
    # Adiciona as palavras digitadas a uma lista
    lista_palavra.append(palavra)
    #Pede para o usuário escolher outra palavra
    palavra=input('Digite outra palavra:')

#Imprime apenas as palavras que começam com 'a'    
i = 0
#Determina a condição do loop
while i < len(lista_palavra):
    # cria uma variável com os elementos da lista
    palavra = lista_palavra[i]
    # verifica se a palavra começa com a
    if len(palavra)>0 and palavra[0] == 'a':
        print(palavra)
    i = i + 1
    
    