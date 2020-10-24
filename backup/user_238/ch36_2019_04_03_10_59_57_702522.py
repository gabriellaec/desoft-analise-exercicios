def eh_primo(numero):
    i=0
    impar=3
    primo='True'

    while i < numero and impar < numero:
        
        if numero !=2:
            if numero % 2 ==0 or numero % impar == 0:
                primo = 'False'
        
        i+=1
        impar+=2
    return primo

print(eh_primo(13))
print(eh_primo(2))
print(eh_primo(8))
