with open(churras.txt,"r") as arquivo:
    conteudo = arquivo.readlines()
    
    separando = conteudo.split(";")
    A = int(separando[1])
    B = float(separando[2])
    
    separando[1] = A
    separando[2] = B
    
    print(B)