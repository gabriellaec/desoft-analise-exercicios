def eh_bissexto(x):
    return (x%4==0)
def eh_ou_não(x):
    if eh_bissexto(x):
        return "SIM"
    else:
        return "NÃO"
print (eh_ou_não(100))