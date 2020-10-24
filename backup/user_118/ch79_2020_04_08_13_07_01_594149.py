def monta_dicionario(telefone):
    agenda = {"Fulano": "99999-1111", "Sicrano": "99999-2222"}
    if telefone in agenda:
        return agenda[telefone]