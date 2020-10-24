string = input('Digite algo: ')
def palindromo(string):
    if (string==string[::-1]):
        return True
    else:
        return False
print(palindromo(string))