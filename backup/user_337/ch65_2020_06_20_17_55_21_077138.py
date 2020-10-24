def capitaliza(string):
    a = len(string)
    b = string[:1]
    string2 = b.upper()+string[1:a]
    return string2