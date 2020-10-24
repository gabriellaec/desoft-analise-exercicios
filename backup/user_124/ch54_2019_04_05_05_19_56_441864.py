def junta_nome_sobrenome(nome , sobrenome):
    nome = []
    sobrenome = []
    contador = 0
while contador < len(nome) and contador < len(sobrenome):
    nome_completo = nome[contador] + sobrenome [contador]
    contador += 1
return nome_completo