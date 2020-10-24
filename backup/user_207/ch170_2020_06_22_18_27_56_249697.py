def apaga_repetidos (string):
    # Encontra onde repete a primeira vez
    # Splita (fatiamente)
    # Substitui todas as repetições na segunda metade
    # Junta
    # Analisa outro caractere
    new_string = string
    base = 0
    while base < len(string) -1:
        i = 0
        while i < len(string):
            
            if new_string[base] == '*':
                i += 1

            elif new_string[base] == new_string[i]:
                # Fatia
                inicio = new_string[:i+1]
                fim = new_string[i+1:]
                novo_fim = fim.replace(new_string[base], '*')

                #print (inicio)
                #print (novo_fim)
                new_string = inicio + novo_fim
                i += 1

            else:
                i += 1
        base += 1

    return new_string