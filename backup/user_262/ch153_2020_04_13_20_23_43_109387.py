def agrupa_por_idade(nome:idade):
    if idade<11:
        return 'criança : [%f]'%(nome)
    else:
        if 12<=idade<=17:
            return 'adolescente : ['nome']'
            
        else:
            if 18<=idade<=59:
                return 'adulto : ['nome']'
            
            else:
                return 'idoso['nome']'