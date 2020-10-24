#def login_disponivel(string,lista):
 #   v=1
  #  o=True
   # while o:
    #        if string not in lista:
     #           return string
      #          o=False
       #     else:
        #        return string+f"{v}"
         #       v+=1
def login_disponivel(string, lista):
    if string not in lista:
        return login
    else:
        x = 1
        while True:
            if string + str(x) not in lista:
                return string + str(x)
            else:
                x += 1