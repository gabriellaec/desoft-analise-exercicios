bissexto = True 
def ano_bissexto(ano, x):
    if x * 100 != ano:
        if x * 400 == ano:
            if ano % 4 == 0:
                return True
    else:
        bissexto == False