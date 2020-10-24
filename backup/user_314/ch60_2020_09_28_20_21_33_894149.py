def eh_palindromo (str):
    i=0
    while(i<len(str)):
        
        if(str[i]!=str[len(str)-i-1]):
            return False
        i+=1

    return True