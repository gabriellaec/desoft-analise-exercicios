def eh_bissexto (ano_eh_bissexto):
    if ano % 400 == 0 and ano % 100 == 0 and ano % 4 == 0:
        return True
    else:
        return False