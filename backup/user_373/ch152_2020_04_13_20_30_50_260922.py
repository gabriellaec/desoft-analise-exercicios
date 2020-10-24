t: {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
c: {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }

def verficica_preco (t,c):
    v= 0.0
    for livro in t :
        if t in c:
            v+= c[livro]
    return v
            