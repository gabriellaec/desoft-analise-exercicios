def verifica_preco(nome):
    nomes = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    precos = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    escolha = input("escolha o seu livro")
    if escolha in nomes:
        return nomes.keys(nomes[escolha])
    return precos.keys(nomes.keys(nomes[escolha]))