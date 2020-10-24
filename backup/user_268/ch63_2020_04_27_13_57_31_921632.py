def nome_usuario(em):
    a = em.find('@')
    nome = em[:a]
    return nome
    