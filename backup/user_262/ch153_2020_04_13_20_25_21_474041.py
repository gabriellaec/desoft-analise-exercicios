def agrupa_por_idade(nome:idade):
    if idade<11:
        return 'criança : [%f]'%(nome)
    else:
        if 12<=idade<=17:
            return 'adolescente : [%f]'%(nome)
            
        else:
            if 18<=idade<=59:
                return 'adulto : [%f]'%(nome)
            
            else:
                return 'idoso[%f]'%(nome)