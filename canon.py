import random

msgs1Tiro = ["as alcanzado al enemigo","as herido al enemigo","you lose"]
msgs2Tiro = ["un herido uno fuera del mapa","que mala punteria tienes","inpresionante el otro barrio necesita 2 casas mas"]

def mensage1():
    mes1 = random.choice(msgs1Tiro)
    print(mes1)

def mensage2():
    mes2 = random.choice(msgs2Tiro)
    print(mes2)


def runMainFunccion():
    disparo = (input("introduce el numero de disparos(1o2) y la direccion(delante:w a la derecha:d a la izquierda:a detras:s): "))

    if disparo == "1w":
        mensage1()

    elif disparo == "1d":
        mensage1()

    elif disparo == "1s":
        mensage1()

    elif disparo == "1a":
        mensage1()

    elif disparo == "2w":
        mensage2()

    elif disparo == "2d":
        mensage2()

    elif disparo == "2s":
        mensage2()

    elif disparo == "2a":
        mensage2()

    else:
        print("no es lo que te dije ")   

def checkExit():
    resp = ""

    while (resp != "n" and resp != "s"):
        resp = input("quieres seguir disparando? [s/n]")
        if resp == "n" : 
            return False
    return True

running = True
while running :
    runMainFunccion()
    running = checkExit()