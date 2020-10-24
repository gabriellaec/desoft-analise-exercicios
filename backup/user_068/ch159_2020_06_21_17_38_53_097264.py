import json
with open('estoque.json', 'r') as arquivo.json:
    texto = arquivo_json.read()
print(texto)
dicionario = json.loads(texto)
# Transformando de volta para JSON (texto)
novo_json = json.dumps(dicionario)
# Salvando o arquivo
with open('alunos.json', 'w') as arquivo_json:
arquivo_json.write(novo_json)
# Abra o arquivo alunos.json e verifique seu conteúdo.
b = novo_json.split()
i=0
while i < len(b):
    total = b[i]*b[i+1]
    b+=2
    