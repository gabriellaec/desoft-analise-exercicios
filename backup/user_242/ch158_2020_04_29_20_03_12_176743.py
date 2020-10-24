def conta_palavras(nome): 
    with open (nome,'r') as arquivo:    #Abrir arquivo para ler
        conteudo = arquivo.read()       #Ler o arquivo e põe dentro da variável conteúdo
        palavras = conteudo.split()     #sendo uma string pode usar split
        return len(palavras)

print(conta_palavras("texto.txt"))  
    