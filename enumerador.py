#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for num,nombre in enumerate(lista_nombres):

    if nombre[0] == 'M':
         print(num)
    else:
        continue


# for nombre in lista_nombres:
#     if nombre[0] == 'M':
#          print(nombre)
#     else:
#         continue



#-----------------------------------------------------------------------------

# mi_lista = []
#
# for x,y in enumerate("Python"):
#     agregar_tuple = (x,y)
#     mi_lista.append(agregar_tuple)
#
# lista_indices = mi_lista
#
# print(type(lista_indices))


#-----------------------------------------------------------------------------
# mi_lista = []
#
# for x in "Python":
#     mi_lista.append(x)
#     print(mi_lista)
#
# mi_tuple = tuple(mi_lista)
#
# print(mi_tuple)

#-----------------------------------------------------------------------------

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#
#
# for indice,nombre in enumerate(lista_nombres):
#
#     print(f'{nombre} se encuentra en el índice {indice}')

#-----------------------------------------------------------------------------

# lista = ["a","b","c"]
#
# mis_tuples = list(enumerate(lista))
#print(mis_tuples)


# for x,item in enumerate(lista):
#     print(x,item)

#metodo mas largo
# for item in enumerate(range(50,55)):
#     print(item)
#