##Tres en raya
## Probando git, probando, probando...

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
    posicion5 = True
    jugadasM.append(5)
    return posicion5

def mostrarCasillaOcupada():
    print("la casilla está ocupada")

def guardarJugada(jugada, contador, jugadasM, jugadasJ):
    if comprobarJugada(jugada, contador):
        if contador % 2 == 0:
            jugadasM.append(jugada)
            contador = contador + 1
        else:
            jugadasJ.append(jugada)
            contador = contador + 1
    return contador

def comprobarJugada(jugada, contador):
    if contador % 2 != 0:
        
        if jugada == 5:
            mostrarCasillaOcupada()
            return False
        else:
            return True    



# def pintarJugadas(a, b, c, d, e, f, g, h, i):
#     if e == True and a






maquina = "X"
jugador = "O"
jugadasM = []
jugadasJ = []
contador = 1 #jugadas pares para la máquina, las impares para el humano
control = False
posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("juguemos al tres en raya, primero muevo yo:")
posicion5 = iniciarJuego(posiciones[4], jugadasM)

while control == False:
    jugada = int(input("Elige la posición que quieres ocupar: "))
    if 1<=jugada<=9:
        control = guardarJugada(jugada, contador, jugadasM, jugadasJ)
    else:
        print("La opción no se encuentra disponible")   

print(jugadasJ)
print(contador)
print(control)