txt="123456789"
def esconde_senha(txt):
    i=0
    while i<len(txt):
        if txt[i]!='*':
            txt[i]="*"
        i+=1
    return txt
print (esconde_senha(txt))
