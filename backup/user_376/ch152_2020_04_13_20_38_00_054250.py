def verifica_preco(livro):
    l={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    p={"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    if livro in l:
        procura=l[livro]
        proc=procura[1]
        if proc in p:
            preco=p[proc]
            return preco{1}