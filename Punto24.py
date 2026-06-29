# Pila de personajes
pila = []

# Cargar personajes
pila.append(("Iron Man", 10))
pila.append(("Capitan America", 11))
pila.append(("Rocket Raccoon", 6))
pila.append(("Groot", 5))
pila.append(("Black Widow", 9))
pila.append(("Doctor Strange", 6))
pila.append(("Gamora", 4))
pila.append(("Capitana Marvel", 3))

# Pila auxiliar
aux = []

posicion = 1
pos_rocket = -1
pos_groot = -1

print("Los personajes que participaron en más de 5 películas:")

while len(pila) > 0:

    personaje = pila.pop()

    nombre = personaje[0]
    peliculas = personaje[1]

    # Punto a
    if nombre == "Rocket Raccoon":
        pos_rocket = posicion

    if nombre == "Groot":
        pos_groot = posicion

    # Punto b
    if peliculas > 5:
        print(nombre, "-", peliculas, "películas")

    # Punto c
    if nombre == "Black Widow":
        print("\nBlack Widow participó en", peliculas, "películas")

    # Punto d
    if nombre.startswith(("C", "D", "G")):
        print("Empieza con C, D o G:", nombre)

    aux.append(personaje)

    posicion += 1

# Restaurar la pila
while len(aux) > 0:
    pila.append(aux.pop())

print("\nRocket Raccoon está en la posición:", pos_rocket)
print("Groot está en la posición:", pos_groot)