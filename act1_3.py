#1. Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno utilizando un bucle

lista_estudiantes = ["Euriel", "Juan", "Maria", "Ana", "Luis"]
for estudiante in lista_estudiantes:
    print(f"Estudiante: {estudiante}")

#2. Crear un diccionario simple que almacene información de contacto (nombre,correo) y mostrar sus claves y valores. 
contacto = {
    "nombre": "Euriel",
    "correo": "eurielcorrea@gmail.com"
}
print("\nInformación de contacto:")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

#3. Implementar un script que permita al usuario agregar elementos a una lista o actualizar valores en un diccionario. 

lista = [] # Lista para almacenar elementos
diccionario = {"sopa": 1500, "arroz": 3000} # Diccionario para almacenar claves y valores

while True:
    print("\n--- Menú ---")
    print("1. Agregar elemento a la lista")
    print("2. Actualizar valor en el diccionario")
    print("3. Mostrar lista y diccionario")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        elemento = input("Ingresa un elemento para agregar a la lista: ")
        lista.append(elemento)
        print("Elemento agregado.")
    
    elif opcion == "2":
        clave = input("Ingresa la clave del diccionario: ")
        valor = input("Ingresa el valor asociado a la clave: ")
        diccionario[clave] = valor
        print("Diccionario actualizado.")
    
    elif opcion == "3":
        print(f"\nLista actual: {lista}")
        print(f"Diccionario actual: {diccionario}")
    
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")
