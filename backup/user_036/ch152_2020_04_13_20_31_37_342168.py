livro = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cor = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0}
titulo = 'Dom Quixote'
def verifica_preco(titulo):
    for titulo in livro.values():
        return(cor[titulo])
print(verifica_preco(titulo))