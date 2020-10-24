n = 0
expressao = 1
while n < 100:
    expressao = 1/(2**(n+1)) + expressao
    n = n + 1
print(expressao)