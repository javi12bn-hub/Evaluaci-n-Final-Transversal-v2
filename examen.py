peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

#opcion 1
def cupos_genero(genero):
    for codigo in peliculas:
        genero_buscado = peliculas[codigo][1]
        if genero.strip().lower() == genero_buscado:
            cupos_carte = cartelera[codigo][1]
            if cupos_carte > 0:
                print(f"Existen {cupos_carte} cupos disponibles")
            else:
                print("No hay cupos disponibles")

#opcion 2
def busqueda_precio(p_min, p_max, cartelera, peliculas):
    lista_buscados = []
    for codigo, codigo_cartelera in cartelera.items():
        precio = codigo_cartelera[0]
        cupos_carte = codigo_cartelera[1]
        if precio >= p_min and precio <= p_max and cupos_carte > 0:
            titulo = peliculas[codigo][0]
            lista_buscados.append(f"{titulo}--{codigo}")
    if len(lista_buscados) < 0:
        print("No hay películas en ese rango de precios.")
    else:
        lista_buscados.sort()
        print(lista_buscados)

#opcion 3
def actualizar_precio(codigo, nuevo_precio, cartelera):
    codigo = codigo.strip().upper()
    if codigo in cartelera:
        cartelera[codigo][0] == nuevo_precio
        return True
    else:
        return False

#opcion 5
def eliminar_pelicula(codigo):
    if codigo in peliculas: 
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False

def leerOpcion():
    print("=======MENÚ PRINCIPAL========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("===========================")
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion < 0 or opcion > 6:
            print("Debe seleccionar una opción válida. ")
        else:
            return opcion
    except ValueError:
        print("Debe seleccionar una opción válida. ")

while True:
    opcion = leerOpcion()
    #-------------------
    if opcion == 1:
        genero = input("Ingrese género a buscar: ")
        cupos_genero(genero)
    #---------------
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese el precio mínimo: "))
            p_max = int(input("Ingrese el el precio máximo: "))
            if p_min <= 0 and p_max <= 0 or p_min > p_max:
                print("Debe ingresar valores enteros.")
            else:
                busqueda_precio(p_min, p_max, cartelera, peliculas)
        except ValueError:
            print("Debe ingresar valores enteros.")
        print()
    #-----------------
    elif opcion == 3:
        while True:
            codigo = input("Ingrese el código de la película: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if nuevo_precio <= 0:
                    print("Debe de ingresar un valor mayor a 0")
                    continue
                actualizar = actualizar_precio(codigo, nuevo_precio, cartelera)
                if actualizar == True:
                    print("Precio actualizado.")
                elif actualizar == False:
                    print("El código no existe")
                break
            except ValueError:
                print("Debe ingresar un número entero.")
            
    #-----------------
    elif opcion == 4:
        print()
    #--------------------
    elif opcion == 5:
        codigo = input("Ingrese el código de la película a eliminar: ").upper()
        eliminar_pelicula(codigo)
        if eliminar_pelicula(codigo) == True:
            print("Película eliminada")
        elif eliminar_pelicula(codigo) == False:
            print("El código no existe")
    #---------------------
    elif opcion == 6:
        print("Programa finalizado.")
        break