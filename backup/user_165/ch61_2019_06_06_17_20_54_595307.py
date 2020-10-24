def palindromo(string):
    if (string==string[::-1]):
        return True
    else:
        return False
string = input('Digite algo: ')
print(palindromo(string))