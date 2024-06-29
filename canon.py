import random

msgsTiro = [[
 #1
  {"text": "as alcanzado al enemigo ha muerto", "value": 25},
  {"text": "as herido al enemigo", "value": 10},
  {"text": "you lose", "value": -10},
  {"text": "has herido un amigo eres peor quel diablo", "value":-50},
  {"text": "tienes un oficial fuera oficial:)", "value": 50},
],
 #2
[
  {"text": "un herido uno fuera del mapa", "value": 35},
  {"text": "que mala punteria tienes", "value": -20},
  {"text": "inpresionante el otro barrio necesita 2 casas mas", "value": 50},
  {"text": "un general herido ", "value": 30}
]]


doblones = 0

def calculateDoblones(mes):
    global doblones 
    doblones += mes["value"]
    print(f"doblones actuales: {doblones}")

def mensaje(idx):
    mes = random.choice(msgsTiro[idx])
    print(mes["text"])
    calculateDoblones(mes)

  
opciones_de_tiro = {
    "1w": mensaje,
    "1d": mensaje,
    "1a": mensaje,
    "1s": mensaje,
    "2w": mensaje,
    "2d": mensaje,
    "2a": mensaje,
    "2s": mensaje
}

def runMainFunccion():
    
    disparo = (input("introduce el numero de disparos(1o2) y la direccion(delante:w a la derecha:d a la izquierda:a detras:s): "))
      
    if disparo in opciones_de_tiro:
        d = int(disparo[0])  
        opciones_de_tiro[disparo](d-1)  
        
    else:
        print("no es lo que te dije ")   

def checkExit():
    resp = ""

    while (resp != "n" and resp != "s"):
        resp = input("quieres seguir disparando? [s/n]")
        if resp == "n" : 
            return False
        elif resp == "s":
            return True
        else:
            print ("no es valido introduce s o n")

running = True
while running :
    runMainFunccion()
    running = checkExit()