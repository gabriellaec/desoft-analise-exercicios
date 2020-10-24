def apaga_repetidos(palavra):
    for letra in palavra:
        tutu = ''
        if letra not in tutu:
            tutu += letra 
        else: 
            tutu = tutu.replace(letra,'*',1)

'''Concatenação, 
palavra = ''
for letra in palavra
if letra not in palavra
palavra += letra 
else:
palavra = palavra.replace(,'*')