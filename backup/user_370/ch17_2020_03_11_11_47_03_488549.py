def ano_bissexto (x):
    if x % 4 == 0:
        return True
    else:
        return False
    
print(ano_bissexto (1997))