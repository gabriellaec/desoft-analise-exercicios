import json
with open('estoque.json', 'r') as arquivo:
        conteudo=arquivo.open()
        estoque=json.loads(contuedo)
        total=0
        for p in estoque["produtos"]:
            total+= p["quantidade"] * p["valor"]
        print(total)
      