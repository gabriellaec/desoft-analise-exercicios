n = 0
expressao = 1
for e in range(0,99):
    expressao = 1/(2**(n+1)) + expressao
    n += 1
print(expressao)