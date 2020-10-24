def remove_vogais (string):
    nova=string
    for i in string:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            nova=nova.replace(i,"")
    return nova
