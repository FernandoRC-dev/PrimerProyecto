from random import *

print('\nHe pensado un número entre 1 y 100. \n'
      'Tienes 8 intentos para adivinar cuál es el número secreto. \n')

solucion = randint(1,100)

# print(f'La solucion es {solucion}  #Esta linea es de ayuda a la programación ELIMINAR \n')


intentos_restantes = 8

#pendiente hacer el bucle con contadores de intentos

while intentos_restantes > 0:

    entrada = input("Intenta un numero: ")

    entrada = int(entrada)

    match entrada:

        case entrada if (entrada < 1) or (entrada > 100):
            print("El número elegido está fuera de rango")
            print(f"Intentos restantes: {intentos_restantes-1}\n")

        case entrada if (entrada < solucion):
            print('Respuesta incorrecta, has elegido un número menor al número secreto.')
            print(f"Intentos restantes: {intentos_restantes - 1}\n")

        case entrada if (entrada > solucion):
            print('Respuesta incorrecta, has elegido un número mayor al número secreto.')
            print(f"Intentos restantes: {intentos_restantes - 1}\n")

        case entrada if (entrada == solucion):
            print('Respuesta correcta, ¡has encontrado el número secreto!'
          '¡¡ENHORABUENA!!')

            break

    intentos_restantes -=1

else:
    print(f"Lo siento, se te acabaron las oportunidades. La solución era {solucion}")



# Planteamiento con bucles if

# if ((entrada < 1) or (entrada > 100)):
#     print("El número elegido está fuera de rango")
#
# elif (entrada < solucion):
#     print('Respuesta incorrecta, has elegido un número menor al número secreto')
#
# elif (entrada > solucion):
#     print('Respuesta incorrecta, has elegido un número mayor al número secreto')
#
# elif (entrada == solucion):
#     print('Respuesta correcta, ¡has encontrado el número secreto!\n'
#           '¡¡ENHORABUENA!!')


