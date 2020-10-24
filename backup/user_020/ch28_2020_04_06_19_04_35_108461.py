n = 0
expressao = 1
for e in expressao:
    expressao = 1/(2**(n+1)) + expressao
    n += 1
print(expressao)