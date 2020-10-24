pergunda_número = input('Digiete um número:')
while True:
    if pergunda_número != 0: 
        soma += pergunda_número
        pergunda_número = input('Digiete um número:')
        print (soma)
    else: 
        return False
    
    