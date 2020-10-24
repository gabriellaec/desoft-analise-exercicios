def remove_vogais(palavra):
        i = 0
        lista = []
        while i < len(palavra):
            if palavra[i] != 'a' and palavra[i] != 'e' and palavra[i] != 'i' and palavra[i] != 'o' and palavra[i] != 'u':
                lista.append(palavra[i])
            i += 1
        
        return ''.join(lista)