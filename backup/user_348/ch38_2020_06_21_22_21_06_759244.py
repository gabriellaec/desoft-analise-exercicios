def quantos_uns (numero):
    #Transforma o número inteiro em uma string para assim verificar cada índice
    string = str(numero)
    i = 0
    contador = 0
    while i < len(string):
        # Verifica se o índice atual é igual a 1
        if string[i] == '1':
            # Adiciona 1 ao contador
            contador += 1
        i = i + 1
    return contador
     
        