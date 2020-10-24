def pos_arroba(email):
 #   for i in email:
  #      if 
    i=0
    while i<len(email):
        if email[i]=='@':
            i+=1
            return i