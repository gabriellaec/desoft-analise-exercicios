def login_disponivel(strlog,listalog):
    if strlog not in listalog:
        return strlog
    if strlog in listalog:
        i = 0
        for i in range(strlog):
            strlog[i] = strlog[i+1]
            return strlog
        
       
