def aniversariantes_de_setembro(dic_niver):
    dic_set = {}
    for key, value in dic_niver.items():
        if value[3:5] == "09":
            dic_set[key] = value
    return dic_set

# dic = {
#     "Samanta":"01/01/1999",
#     "Pedro":"12/09/2000",
#     "Timmy":"01/12/1987",
#     "Bob":"30/09/1994",
#     "Patricia":"23/02/1998"
# }

# print(aniversariantes_de_setembro(dic))

# # for key, value in dic.items():
# #     print(key,value[3:5])