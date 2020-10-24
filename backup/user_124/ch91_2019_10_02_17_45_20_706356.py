with open('palavras.txt','r') as arquivo:
    conteudo = arquivo.read()

    def quanto_a(conteudo):
        conteudo = arquivo.read()
        separador = conteudo.split
        contador = 0
        passador = 0
        while passador < len(separador):
            if separador[0] == "a":
                contador += 1
            passador += 1
        return contador