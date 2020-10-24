def remove_vogais(palavra):
        i = 0
        lista = []
        while i < len(palavra):
            if palavra[i] == 'A' or palavra[i] == 'E' or palavra[i] == 'I' or palavra[i] == 'O' or palavra[i] == 'U':
                i += 1
            else:
                lista.append(palavra[i])
                i += 1
        return lista