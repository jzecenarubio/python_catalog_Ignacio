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


def ver_todos():
    if not catalogo:
        print("El catálogo está vacio")
        return

    for nombre, atributos in catalogo.items():
        print(f"\n{nombre}")
        print(f"Compañía: {atributos['compañía']}")
        print(f"Género: {atributos['genero']}")
        print(f"Año: {atributos['año']}")
        print(f"Popularidad: {atributos['popularidad']}")
        print(f"Jugado: {'Sí' if atributos['jugado'] else 'No'}")


def modificar_elemento():
    nombre = input("¿Qué videojuego quieres modificar?: ")

    if nombre not in catalogo:
        print("Ese videojuego no está en el catálogo.")
        return

    print(f"Atributos de '{nombre}': ")
    for atributo, valor in catalogo[nombre].items():
        print(f"{atributo}: {valor}")

    atributo = input("¿Qué atributo quieres modificar (compañía/genero/año/popularidad/jugado)?: ")

    if atributo not in catalogo[nombre]:
        print("Ese atributo no existe para este juego.")
        return

    nuevo_valor = input(f"Nuevo valor para '{atributo}': ")

    if atributo == "año":
        nuevo_valor = int(nuevo_valor)
    elif atributo == "jugado":
        nuevo_valor = nuevo_valor.lower() == "si"

    catalogo[nombre][atributo] = nuevo_valor
    print(f"'{atributo}' de '{nombre}' fue actualizado a: {nuevo_valor}")


def menu():
    while True:
        print("\n+++ CATALOGO DE VIDEOJUEGOS +++")
        print("1. Ver todos los elementos")
        print("2. Agregar un elemento nuevo")
        print("3. Modificar un elemento existente")
        print("4. Salir")

        opcion = input("Elige una opcion: ")


        if opcion == "1":
            ver_todos()
        elif opcion == "2":
            agregar_elemento()
        elif opcion == "3":
            modificar_elemento()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("La opción es invalida, intenta de nuevo")

menu()