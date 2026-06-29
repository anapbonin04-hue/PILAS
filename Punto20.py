
pila = []

opuestas = {                   
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

n = int(input("Ingrese la cantidad de movimientos: "))


for i in range(n):
    print("\nMovimiento", i + 1)

    pasos = int(input("Cantidad de pasos: "))
    direcc = input("Direccion: ").lower()

    
    pila.append((pasos, direcc))

print("\nRecorrido realizado:")
for movimiento in pila:
    print(movimiento[0], "pasos hacia", movimiento[1])


print("\nCamino para volver al punto de partida:")

while len(pila) > 0:
    pasos, direcc = pila.pop()
    print(pasos, "pasos hacia", opuestas[direcc])
pila = []


opuestas = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}


n = int(input("Ingrese la cantidad de movimientos: "))


for i in range(n):
    print("\nMovimiento", i + 1)

    pasos = int(input("Cantidad de pasos: "))
    direcc = input("Direccion: ").lower()

    
    pila.append((pasos, direcc))

print("\nRecorrido realizado:")
for movimiento in pila:
    print(movimiento[0], "pasos hacia", movimiento[1])


print("\nCamino para volver al punto de partida:")

while len(pila) > 0:
    pasos, direcc = pila.pop()
    print(pasos, "pasos hacia", opuestas[direcc])