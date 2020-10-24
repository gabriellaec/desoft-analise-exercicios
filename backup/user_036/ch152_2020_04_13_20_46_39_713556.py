livro = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cor = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0}
titulo = 'O Pequeno Príncipe'
def verifica_preco(titulo, cor, livro):
    nome = livro[titulo]
    for titulo in livro.keys():
        return(cor[nome])
print(verifica_preco(titulo, cor, livro))