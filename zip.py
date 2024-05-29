#----------------------------------------------------------------------------

espanol = ('uno', 'dos', 'tres', 'cuatro', 'cinco')
portugues = ('um', 'dois', 'très','quatro', 'cinco')
english = ('one','two','three','four','five')

uno = ('uno', 'um', 'one')
dos = ('dos', 'dois', 'two')
tres = ('tres', 'três', 'three')
cuatro = ('cuatro', 'quatro', 'four')
cinco = ('cinco', 'cinco', 'five')

combinado = list(zip(espanol,portugues,english))

print(combinado)


#----------------------------------------------------------------------------

# marcas = ('iPhone', 'Samsung', 'Motorola')
# productos = (10, 'Galaxy 10', 'One Zoom')
#
# combinados = list(zip(marcas,productos))
#
# print(combinados)

#----------------------------------------------------------------------------

# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
#
# combinados = zip( capitales, paises)
#
# for capitales, paises in combinados:
#     print(f'La capital de {paises} es {capitales}')

#----------------------------------------------------------------------------

# nombres = ['Ana', 'Hugo', 'Valeria']
# edades = [65,29,42]
# ciudades = ['Lima', 'Madrid', 'Mexico']
# combinados = list(zip(nombres,edades, ciudades))
#
# print(combinados)
#
# for nombre, edad, ciudad in combinados:
#     print(f'{nombre} tiene {edad} años y vive en {ciudad}')