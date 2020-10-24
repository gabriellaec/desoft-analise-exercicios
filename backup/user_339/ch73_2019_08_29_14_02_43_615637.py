def remove_vogais(texto):
     
    vogais = ['a','e','i','o','u']
    s = ''
    
    for letra in texto:
        if letra not in vogais:
            s += letra
    return s
        
x = remove_vogais('abacaxi')       
print(x)