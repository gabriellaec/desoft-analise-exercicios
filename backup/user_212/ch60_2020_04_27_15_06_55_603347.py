def eh_palindromo(string):
    i=0
    fim=len(string)-1
    while i<len(string):
        if string[i] == string[fim-i]:
            return True 
        elif string[i] != string[fim-i]:
            return False 
        i +=1