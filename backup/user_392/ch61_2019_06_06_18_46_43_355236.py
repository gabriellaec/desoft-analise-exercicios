def eh_palindromo(palavra):
    inver = palavra[: : -1]
    nor = palavra[: : 1]
    if inver == nor:
        return True
    else:
        return False
    
    
    