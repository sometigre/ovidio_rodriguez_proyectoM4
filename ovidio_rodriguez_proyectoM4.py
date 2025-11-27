# Importamos la libreria requests para poder consumir la pokeapi
import requests
import os
import json

# Creamos la carpeta donde se guardaran los datos si no existe
if not os.path.exists("pokedex"):
    os.mkdir("pokedex")

# Funcion que extrae los tipos
def obtener_tipos(data):
    tipos = []
    for tipo in data["types"]:
        tipos.append(tipo["type"]["name"])
    return tipos

# Funcion que extrae las habilidades
def obtener_habilidades(data):
    habilidades = []
    for hab in data["abilities"]:
        habilidades.append(hab["ability"]["name"])
    return habilidades

# Funcion que extrae los movimientos
def obtener_movimientos(data):
    movimientos = []
    for mov in data["moves"]:
        movimientos.append(mov["move"]["name"])
    return movimientos

# Funcion principal que busca un pokemon
def buscar_pokemon(nombre):
    # Creamos la url con el nombre que escriba el usuario, la url para acceder al API es: https://pokeapi.co/
    url = "https://pokeapi.co/api/v2/pokemon/" + nombre.lower()

    # Hacemos la peticion GET
    respuesta = requests.get(url)

    # Verificamos el codigo de estado
    if respuesta.status_code == 200:
        # Convertimos la respuesta en json
        datos = respuesta.json()

        # Extraemos los datos necesarios
        info_pokemon = {}
        info_pokemon["nombre"] = datos["name"]
        info_pokemon["peso"] = datos["weight"]
        info_pokemon["altura"] = datos["height"]
        info_pokemon["tipos"] = obtener_tipos(datos)
        info_pokemon["habilidades"] = obtener_habilidades(datos)
        info_pokemon["movimientos"] = obtener_movimientos(datos)
        info_pokemon["imagen"] = datos["sprites"]["front_default"]

        # Mostramos los datos
        print("Nombre:", info_pokemon["nombre"])
        print("Peso:", info_pokemon["peso"])
        print("Altura:", info_pokemon["altura"])
        print("Tipos:", ", ".join(info_pokemon["tipos"]))
        print("Habilidades:", ", ".join(info_pokemon["habilidades"]))
        print("Imagen:", info_pokemon["imagen"])

        # Guardamos en un archivo json
        archivo = open("pokedex/" + nombre.lower() + ".json", "w")
        json.dump(info_pokemon, archivo, indent=4)
        archivo.close()

        print("Los datos se guardaron correctamente en la carpeta pokedex")

    else:
        print("Error: No se encontro el pokemon o hubo un problema con la API")

# Pedimos al usuario que escriba el nombre
nombre_pokemon = input("Escribe el nombre del Pokemon que quieres buscar: ")
buscar_pokemon(nombre_pokemon)
