def simplifica_dict(dic): 
    dict = {}
    dict['felipe']="lacombe"
    dict['ohara']="shiba"
    dict_lista=[]
    for k,v in dict.iteritems():
        dict_lista.append ((k,v))
    print (dict_lista)