preco = 0
with open('churras.txt', 'r') as arquivo:
    
    content = arquivo.readlines()
    
    for line in content:
        
        lista = line.split(',')
        
        mult = int(lista[1])
        print(mult)
        
        produto = float(lista[2].strip())
        print(produto)
        
        preco += mult*produto
        
print(preco)