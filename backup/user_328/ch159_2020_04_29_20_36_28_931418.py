#exercicio da video aula
import json
with open('estoque.json', 'r') as arquivo_js:
    conteudo= arquivo_js.read()
    estoque= json.loads(conteudo)
    total= 0
    for o in estoque['produtos']:
        total += o['quantidade'] * o['preco']
    print(total)