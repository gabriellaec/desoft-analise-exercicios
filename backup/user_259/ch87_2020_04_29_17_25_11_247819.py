soma = 0
with open('churras.txt') as churras:
    linhas = churras.readlines()
    for linha in linhas:
        virgula = linha.find(',')
        linha = linha[virgula+1:]
        virgula = linha.find(',')
        new_line = linha.find('\n')
        soma+= int(linha[0])*int(linha[virgula+1:new_line])