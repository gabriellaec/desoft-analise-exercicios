def eh_bissexto(jaca):
    resto=ano%4
    if(resto==0):
        return True
    else:
        return False
print(eh_bissexto(3))