def eh_palindromo(palavra):
    i=0
    while i<len(palavra):
        if palavra[i]==palavra[-i]:
             return True
            i+=1
       
    