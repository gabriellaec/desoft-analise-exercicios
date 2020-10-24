def adivinhe_a_palavra(x):
    if x == 'desisto':
        return 'Você acertou a senha!'
    else:
        return 'Errado, tente denovo'
    
word=str(input('Palavra desejada: '))

print (adivinhe_a_palavra(word))