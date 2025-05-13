#código del desafío 27 Bruno Almonacid en el código de búsqueda y registro y juanita monzón en el menu
ciudad = []
def registrarCiudad(ciudades, nombre, poblacion, autosustentabilidad, amenaza):
    ciudad = {"nombre": nombre,"poblacion": poblacion,"autosustentabilidad": autosustentabilidad,"amenaza": amenaza}
    ciudades.append(ciudad)
    return ciudades
def clasificarPorAutosustentabilidad(ciudades):
    return sorted(ciudades, key=lambda x: x["autosustentabilidad"], reverse=True)
"""respuesta a la pregunta de la profe en la ultima clas:
key=lambda x: x es una expresión común utilizada como argumento en funciones que admiten un parámetro key
como sorted, min, y max. Esta expresión define una función anónima (lambda)que devuelve su argumento sin modificarlo.
"""
def buscarPorAmenaza(ciudades, amenaza):
     resultado = []
     for ciudad in ciudades:
         if ciudad["amenaza"] == amenaza:
             resultado.append(ciudad)
     return resultado

#menu
def menu():
    ciudades = []
    while True:
        print("\n🌆--- Registro de Ciudades Posapocalípticas ---🌆")
        print("1. 📖 Registrar ciudad")
        print("2.🌱 Mostrar ciudades clasificadas por autosustentabilidad")
        print("3. ⚠ Buscar ciudades por tipo de amenaza externa")
        print("4. 🏃 Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la ciudad:")
            poblacion = int(input("Población:"))
            autosustentabilidad = int(input("Nivel de autosustentabilidad (1-10):"))
            amenaza = input("Tipo de amenaza externa: ")
            ciudades = registrarCiudad(ciudades, nombre, poblacion, autosustentabilidad, amenaza)
            print("Ciudad registrada con éxito.")
        elif opcion == "2":
            clasificadas = clasificarPorAutosustentabilidad(ciudades)
            print("\nCiudades clasificadas por autosustentabilidad:")
            for ciudad in clasificadas:
                print(f"📍{ciudad['nombre']} - 🌱 Autosustentabilidad: {ciudad['autosustentabilidad']}")
        elif opcion == "3":
            amenaza = input("Tipo de amenaza externa a buscar:")
            resultado = buscarPorAmenaza(ciudades, amenaza)
            print("\n ⚠ Ciudades por amenaza externa:", amenaza)
            for ciudad in resultado:
                print(f"📍{ciudad['nombre']} - 👥 Población: {ciudad['poblacion']}")
        elif opcion == "4":
            print("🏃 Saliendo del programa. Mebi oso na hit choda op nodotaim 🤝")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
    """respueta a la pregunta de la profe en la ultima clas:
es una construcción común en Python que se utiliza para determinar si un archivo está 
siendo ejecutado directamente o si está siendo importado como un módulo en otro archivo."""