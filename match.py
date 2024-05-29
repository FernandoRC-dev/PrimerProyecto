def describe_variable(variable):
    match variable:
        case int():
            print("La variable es un entero.")
        case str():
            print("La variable es una cadena.")
        case list():
            print("La variable es una lista.")
        case _:
            print("La variable es de un tipo diferente.")

# Ejemplos de uso
describe_variable(10)      # La variable es un entero.
describe_variable("hola")  # La variable es una cadena.
describe_variable([1, 2, 3])  # La variable es una lista.
describe_variable(3.14)    # La variable es de un tipo diferente.
