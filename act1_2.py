#1. script de numero par o impar

numero = int(input("Inserte un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#implemetacion de bucle for
numero = [1,2,3,4,5] #lista de numeros
for n in numero:
    print(f"El cuadrado de {n} es: {n**2}")

# Implementación de bucle while
# Ejemplo: seguir pidiendo una palabra hasta que el usuario escriba "salir"
entrada = ""

while entrada.lower() != "salir":
    entrada = input("Escribe algo (escribe 'salir' para terminar): ")
    print(f"Has escrito: {entrada}")

print("Has salido del bucle. ¡Adiós!")
