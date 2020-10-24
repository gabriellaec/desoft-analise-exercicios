import json
valor_total = 0
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
dict = json.loads(texto)
#dividindo por linhas
X = dict["produtos"]
for elemento in X:
    A = elemento["quantidade"]
    B = elemento["valor"]
    valor = A*B
    valor_total += valor
print(valor_total)