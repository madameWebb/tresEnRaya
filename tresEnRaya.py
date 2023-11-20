##Tres en raya
import random

def jugarMaquina(contador, posiciones, jugadasM):
    if contador == 0:
        jugadasM.append(5)
        posiciones[4] = "X"
        contador +=1
    else:
        while True:
            jugada = random.randint(1, 9)
            if comprobarJugada(jugada, posiciones):
                jugadasM.append(jugada)
                posiciones[jugada - 1] = "X"
                break
        contador +=1
    return contador

def comprobarJugada(jugada, posiciones):
    if not (jugada == posiciones[jugada - 1]):
        return False
    else:
        return True    

def jugarHumano(contador, posiciones, jugadasJ):
    while True:
        try:
            jugada = int(input("Elige la posición que quieres ocupar: "))
            if 1<=jugada<=9:
                if comprobarJugada(jugada, posiciones):
                    jugadasJ.append(jugada)
                    posiciones[jugada - 1] = "O"
                    break
                else:
                    print("la casilla está ocupada")
            else:
                print("La opción no se encuentra disponible") 
        except ValueError:
            print("Debes introducir un número entre el 1 y el 9, ambos incluidos") 
    contador += 1
    return contador
        
def comprobarFinJuego(jugadas, combinaciones):
    for j in range(len(combinaciones)):
        aciertos = 0
        for k in range(len(combinaciones[j])):
            if combinaciones[j][k] in jugadas:
                aciertos += 1
            if aciertos == 3:
                return True


def mostrarTablero(posiciones):
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[0], " |  ", posiciones[1], " |  ", posiciones[2], " |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[3], " |  ", posiciones[4], " |  ", posiciones[5], " |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[6], " |  ", posiciones[7], " |  ", posiciones[8], " |")
    print("|      |      |      |")
    print("+------+------+------+")



jugadasM = []
jugadasJ = []
contador = 0 #jugadas pares para la máquina, las impares para el humano
posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinaciones = [[1, 2, 3],
                 [4, 5, 6], 
                 [7, 8, 9],
                 [1, 4, 7],
                 [2, 5, 8],
                 [3, 6, 9],
                 [1, 5, 9],
                 [3, 5, 7]]

mostrarTablero(posiciones)

print("juguemos al tres en raya, primero muevo yo:")


while contador < 9:
    contador = jugarMaquina(contador, posiciones, jugadasM)
    mostrarTablero(posiciones)
    if comprobarFinJuego(jugadasM, combinaciones):
        print("Gané, fin del juego")
        break
    if contador != 9:
        contador = jugarHumano(contador, posiciones, jugadasJ)
        mostrarTablero(posiciones)
        if comprobarFinJuego(jugadasJ, combinaciones):
            print("Ganaste, Persona, fin del juego")
            break
        print("Ahora me toca a mi:")
    else:
        print("fin del juego, resultado: Tablas")
