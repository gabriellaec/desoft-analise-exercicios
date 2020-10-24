def login_disponivel(L):
    Login=str(input("Digite o login que queira fazer no site:"))
    if Login == "fim":
        return(L)
    elif Login != "fim":    
        i=0
        while i<len(L):
            if Login not in L:
                L.append(Login)
                Login=str(input("Digite o login que queira fazer no site:"))
                if Login == "fim":
                    return(L)
            elif Login+str(i) not in L:
                L.append(Login+str(i))
                Login=str(input("Digite o login que queira fazer no site:"))
                if Login == "fim":
                    return(L)
            else:
                i+=1