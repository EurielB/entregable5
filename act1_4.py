#CALCULADORA DE
def realizar_operacion(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 == 0:
            return "Error: División por cero."
        return num1 / num2
    else:
        return "Error: Operación no válida."

# Solicitar datos al usuario
print("**Bienvenido a la calculadora.**")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingrese la operación a realizar: \n"+
    "=> suma\n" +
    "=> resta\n"+
    "=> multiplicacion\n"+
    "=> division\n"+
    "=> salir " + "para terminar:").lower()

# Realizar la operación
resultado = realizar_operacion(num1, num2, operacion)
print("Resultado:", resultado)




# Juego de Adivina el Número
import random
 
print("¡Adivina el Número!")
print("He pensado en un número entre 1 y 100.")
 
# 1. Generar un número aleatorio
numero_secreto = random.randint(1, 100) # Rango más pequeño para que sea más rápido
intentos = 0
adivinado = False
 
# 2. Bucle para que el usuario intente adivinar
while not adivinado:
    # 3. Solicitar la entrada del usuario (asumimos que ingresará un número)
    intento_str = input("Introduce tu número: ")
    intentos += 1
 
    # Convertir la entrada a número
    intento_num = int(intento_str)
 
    # 4. Comparar y dar pistas
    if intento_num < numero_secreto:
        print("El número secreto es MAYOR.")
    elif intento_num > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        # 5. El usuario ha adivinado
        adivinado = True
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Lo adivinaste en {intentos} intentos.")
 
print("¡Gracias por jugar!")
 