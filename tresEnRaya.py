##Tres en raya
## Probando git, probando, probando...
import random

def iniciarJuego(posicion5, jugadasM):
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   1  |   2  |   3  |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   4  |   X  |   6  |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   7  |   8  |   9  |")
    print("|      |      |      |")
    print("+------+------+------+")
    posicion5 = "X"
    jugadasM.append(5)
    return posicion5

def mostrarTablero(posiciones):
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[0], " |  ", posiciones[1], " |  ", posiciones[2], " |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[3], " |  ", posiciones[4], " |  ", posiciones[5], " |")
    print("|      |      |      |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", posiciones[6], " |  ", posiciones[7], " |  ", posiciones[8], " |")
    print("|      |      |      |")
    print("|      |      |      |")
    print("+------+------+------+")

def jugarMaquina(contador, posiciones, jugadasM, jugadasJ, controlM):
    if contador == 0:
        guardarJugada(5, contador, jugadasM, jugadasJ, posiciones)
        posiciones[4] = "X"
        contador = contador + 1
        return contador
    else:
        while controlM == False:
            jugada = random.randint(1, 9)
            controlM = guardarJugada(jugada, contador, jugadasM, jugadasJ, posiciones)
        contador = contador + 1
        return contador
        

        

def mostrarCasillaOcupada():
    print("la casilla está ocupada")

def guardarJugada(jugada, contador, jugadasM, jugadasJ, posiciones):
    if comprobarJugada(jugada, posiciones):
        if contador % 2 == 0:
            jugadasM.append(jugada)
            posiciones[jugada - 1] = "O"
            contador = contador + 1
            return True
        else:
            jugadasJ.append(jugada)
            posiciones[jugada - 1] = "X"
            contador = contador + 1
            return True
    return False

def comprobarJugada(jugada, posiciones):
    if (jugada == posiciones[jugada - 1]) == False:
        return False
    else:
        return True    



# def pintarJugadas(a, b, c, d, e, f, g, h, i):
#     if e == True and a






maquina = "X"
jugador = "O"
jugadasM = []
jugadasJ = []
contador = 0 #jugadas pares para la máquina, las impares para el humano
control = False
controlM = False
posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mostrarTablero(posiciones)

print("juguemos al tres en raya, primero muevo yo:")

contador = jugarMaquina(contador, posiciones, jugadasM, jugadasJ, controlM)
mostrarTablero(posiciones)

print(contador)

while control == False:
    jugada = int(input("Elige la posición que quieres ocupar: "))
    if 1<=jugada<=9:
        control = guardarJugada(jugada, contador, jugadasM, jugadasJ, posiciones)
        if not control:
            mostrarCasillaOcupada()
    else:
        print("La opción no se encuentra disponible")   

mostrarTablero(posiciones)

# print("Ahora me toca a mi:")
# contador = jugarMaquina(contador, posiciones, jugadasM, jugadasJ, controlM)


print("controles")
mostrarTablero(posiciones)
print(jugadasJ, "jugadasJ")
print(jugadasM, "jugadasM")
print(contador, "contador")
print(control, "control")