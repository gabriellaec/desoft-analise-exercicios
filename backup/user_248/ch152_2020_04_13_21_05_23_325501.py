def verifica_preco(titulo):
    x=input('Qual o titulo do livro?')
    dic_livros={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    dic_cores={"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    k=dic_livros.key()
    for k,v in dic_livros:
        if k==x:
            v=y
    for a,b in dic_cores:
        if a==y:
            return b
            
           