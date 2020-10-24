def verifica_preco(nome):
    dic_livros={"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    tab_cores= {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }

    for k,v in dic_livros.items():
        if k == nome:
            for key,values in tab_cores.items():
                if key == v:
                    return values
     