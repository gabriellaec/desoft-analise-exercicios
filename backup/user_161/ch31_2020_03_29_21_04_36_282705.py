def eh_primo(x):
    if x <= 1: 
        return False
    if x == 2: 
        return True
    if x%2==0:
        return False
	if x == 49:
        return True
    
    tmp = 3
    while tmp < x: 
        if x%tmp==0:
            return False
        else:
            tmp = tmp + 2
  
    return True    