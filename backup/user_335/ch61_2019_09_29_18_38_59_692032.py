def palindromo (string):
    return string == string[len(string)::-1]

print (palindromo("Roma é amor"))