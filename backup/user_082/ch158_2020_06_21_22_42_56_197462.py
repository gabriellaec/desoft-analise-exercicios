with open ('texto.txt', 'r') as txt:
    conta = txt.read()
palavras = conta.split()
print(len(palavras))