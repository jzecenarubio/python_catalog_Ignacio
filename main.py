catalogo = {
    "Limbus Company": {"compañía": "Project Moon", "genero": "Gacha / RPG táctico", "año": 2022, "popularidad": "niche", "jugado": True},
    "League of Legends": {"compañía": "Riot Games", "genero": "MOBA", "año": 2009, "popularidad": "popular", "jugado": True},
    "Ender Lilies": {"compañía": "Binary Haze Interactive", "genero": "Metroidvania", "año": 2021, "popularidad": "niche", "jugado": False},
    "Hollow Knight": {"compañía": "Team Cherry", "genero": "Metroidvania", "año": 2017, "popularidad": "popular", "jugado": True},
    "Library of Ruina": {"compañía": "Project Moon", "genero": "RPG por turnos / deckbuilder", "año": 2021, "popularidad": "niche", "jugado": True},
    "Code Vein": {"compañía": "Bandai Namco", "genero": "Souls-like", "año": 2019, "popularidad": "niche", "jugado": False},
    "Persona series": {"compañía": "Atlus", "genero": "JRPG", "año": 1996, "popularidad": "popular", "jugado": True},
    "Elden Ring": {"compañía": "FromSoftware", "genero": "Souls-like / mundo abierto", "año": 2022, "popularidad": "popular", "jugado": True},
}

def agregar_elemento():
    nombre = input("Nombre del videojuego: ")

    if nombre in catalogo:
        print("Este videojuego ya existe en el catalogo.")
        return

    compañía = input("Compañia que lo publicó: ")
    genero = input("Género: ")
    año = int(input("Año de publicación: "))
    popularidad = input("¿Es 'popular' o 'niche'?: ")
    jugado_texto = input("¿Ya lo jugaste? (si/no): ")
    jugado = jugado_texto.lower() == "si"

    catalogo[nombre] = {
        "compañía": compañía,
        "genero": genero,
        "año": año,
        "popularidad": popularidad,
        "jugado": jugado
    }

    print(f"'{nombre}' fue agregado al catalogo")

def menu():
    while True:
        print("\n+++ CATALOGO DE VIDEOJUEGOS +++")
        print("1. Ver todos los elementos")
        print("2. Agregar un elemento nuevo")
        print("3. Modificar un elemento existente")
        print("4. Salir")

        opcion = input("Elige una opcion: ")


        if opcion == "1":
            print("...")
        elif opcion == "2":
            agregar_elemento()
        elif opcion == "3":
            print("...")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("La opción es invalida, intenta de nuevo")

    menu()