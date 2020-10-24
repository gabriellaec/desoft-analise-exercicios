pergunda_número = input('Digiete um número:')
while True:
    if pergunda_número != 0: 
        soma += pergunda_número
        pergunda_número = input('Digiete um número:')
    else: 
        return False
print (soma)