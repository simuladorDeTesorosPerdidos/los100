ciudad = []
def registrarCiudad(ciudades, nombre, poblacion, autosustentabilidad, amenaza):
    ciudad = {"nombre": nombre,"poblacion": poblacion,"autosustentabilidad": autosustentabilidad,"amenaza": amenaza}
    ciudades.append(ciudad)
    return ciudades
def clasificarPorAutosustentabilidad(ciudades):
    return sorted(ciudades, key=lambda x: x["autosustentabilidad"], reverse=True)
def buscarPorAmenaza(ciudades, amenaza):
    return [ciudad for ciudad in ciudades if ciudad["amenaza"] == amenaza]
#menu
def menu():
    ciudades = []
    while True:
        print("\n--- Menú ---")
        print("1. Registrar ciudad")
        print("2. Mostrar ciudades clasificadas por autosustentabilidad")
        print("3. Buscar ciudades por tipo de amenaza externa")
        print("4. Salir")
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
                print(f"{ciudad['nombre']} - Autosustentabilidad: {ciudad['autosustentabilidad']}")
        elif opcion == "3":
            amenaza = input("Tipo de amenaza externa a buscar:")
            resultado = buscarPorAmenaza(ciudades, amenaza)
            print("\nCiudades con amenaza externa:", amenaza)
            for ciudad in resultado:
                print(f"{ciudad['nombre']} - Población: {ciudad['poblacion']}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()