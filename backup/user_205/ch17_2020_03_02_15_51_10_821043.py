def eh_bissexto(x):
    return (x%4==0)
def eh_ou_não(x):
    if eh_bissexto(x):
        return True
    else:
        return False
print (eh_ou_não(100))