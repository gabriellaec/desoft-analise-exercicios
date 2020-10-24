def eh_bissexto(ano):
  	bool1 = ano % 4 == 0
    bool2 = ano % 100 == 0
    return bool1 and not bool2
    

