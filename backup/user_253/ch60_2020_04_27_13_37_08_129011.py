def eh_palindromo (palavra):
    i=0
    a=list(palavra)
    while i<= len(a):
        if a[i] == a[len(a) - i]:
            i+=1
            return True
        else: 
            return False