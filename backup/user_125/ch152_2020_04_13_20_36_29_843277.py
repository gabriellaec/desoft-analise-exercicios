livros={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cores={"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
def verifica_preco(livros,dicionario,cores):
    if livros in dicionario:
        cor=dicionario[livros]
    if cor in dicionario_cores:
        return dicionario_cores[cor]