def eh_primo(teste):
    if teste%2==0:
        resultado=False
    else:
        i=1
        while i<teste:
            if teste%i==0:
                resultado=False
                i+=1
            else:
                resultado=True
                i+=1
            i+=1
    return resultado

print(eh_primo(47))
print(eh_primo(100))