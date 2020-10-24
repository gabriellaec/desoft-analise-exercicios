def apaga_repetidos(palavra):
    lista = []
    for letra in palavra:
        if letra not in lista:
            lista.append(letra)
        else: 
            lista.append('*')
    return ''.join(lista)

'''Concatenação, 
palavra = ''
for letra in palavra
if letra not in palavra
palavra += letra 
else:
palavra = palavra.replace(,'*')'''