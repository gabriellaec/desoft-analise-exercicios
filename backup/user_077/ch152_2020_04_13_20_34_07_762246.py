import math 
def verifica_preco(titulo,dicionario,cores):
    titulo="Dom Quixote"
    dicionario={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    cores={"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    a=dicionario[titulo]
    b=cores[a]
    return b

    