def apaga_repetidos(palavra):
    lista = []
    for letra in palavra:
        if letra not in tutu:
            lista.append(letra)
        else: 
            lista.append('*')
    return lista.join()

'''Concatenação, 
palavra = ''
for letra in palavra
if letra not in palavra
palavra += letra 
else:
palavra = palavra.replace(,'*')'''