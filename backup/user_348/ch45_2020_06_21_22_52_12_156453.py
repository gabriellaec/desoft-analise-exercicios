# Cria uma lista vazia onde os números digitados serão adicionados
lista = []
# Cria uma variável de estado
programa = True
#Define a condição do loop
while programa:
    # Cria uma variável para armazenar a resposta do usuário a cada loop
    numeros = int(input('digite um número inteiro: '))
    #Quando o usuário digita um número menor ou igual a 0, o programa para de perguntar mais números
    if numeros <= 0:
        #Os números negativos ou nulos não serão adicionados a lista
        programa = False
    # Adiciona o número digitado à lista
    else:
        lista.append(numeros)

# cria uma lista vazia onde serão adicionados os números em ordem reversa
lista_2 = []
# cria uma variável cujo o valor é o último índice da lista de números
i = len(lista)-1
# Cria uma condição para percorrer a lista de números
while i >= 0:
    # Adiciona de trás pra frente os elementos na nova lista
    lista_2.append(lista)
    i = i - 1
    
