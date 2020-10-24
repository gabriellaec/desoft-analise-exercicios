def verifica_preco(livro,l,p):
    l={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    p={"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    for livro in l:
        for l[livro] in p:
            return p[l[livro]]
            
        