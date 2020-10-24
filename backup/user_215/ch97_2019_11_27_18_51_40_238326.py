def total_do_semestre_por_bairro(dicionario):
        for key in dicionario:
            novo_dicionario[key] = sum(dicionario[key])