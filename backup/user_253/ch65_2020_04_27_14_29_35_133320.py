def capitaliza(line):
    return ''.join( (c.upper() if i == 0 or s[i-1] == ' ' else c) for i, c in enumerate(s) )