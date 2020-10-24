def eh_palindromo (palavra):
    i=0
    a=list(palavra)
    while i<= len(a):
        if palavra[i] == palavra[len(a) - i]:
            i+=1
            return True
        else: 
            return False