def remove_vogais(palavra):
        i = 0
        lista = []
        while i < len(palavra):
            if palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u':
                i += 1
            else:
                lista.append(palavra[i])
                i += 1
        return lista
