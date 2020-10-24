def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        posicao = palavra.find(letra)
        if contador > 1:
            #Troca a letra por '*' em todas ocorrências
            palavra = palavra.replace(letra,'*')

        #Se a primeira ocorrência tiver um asterisco    
        if palavra[posicao] == '*':
            palavra = palavra.replace('*',letra, 1)
            
    return palavra

'''Concatenação, 
palavra = ''
for letra in palavra
if letra not in palavra
palavra += letra 
else:
palavra = palavra.replace(,'*')