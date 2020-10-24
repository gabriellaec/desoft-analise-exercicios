def verifica_preco(escolha,nomes,precos):
    nomes = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    precos = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    if "Dom Quixote" in nomes:
        return precos.keys(nomes.keys(nomes["Dom Quixote"]))
