with open('texto.txt','r') as t:
    texto=t.read()
    s=texto.split( )
    print(len(s))