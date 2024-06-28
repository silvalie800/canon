import random

msgs1Tiro = [
  {"text": "as alcanzado al enemigo ha muerto", "value": 25},
  {"text": "as herido al enemigo", "value": 10},
  {"text": "you lose", "value": -10},
  {"text": "has herido un amigo eres peor quel diablo", "value":-50},
  {"text": "tienes un oficial fuera oficial:)", "value": 50}
]

msgs2Tiro = [
  {"text": "un herido uno fuera del mapa", "value": 35},
  {"text": "que mala punteria tienes", "value": -20},
  {"text": "inpresionante el otro barrio necesita 2 casas mas", "value": 50},
  {"text": "un general herido ", "value": 30}
]

doblones = 0

def calculateDoblones(mes):
    doblones = doblones + mes["value"]

def mensaje1():
    mes = random.choice(msgs1Tiro)
    print(mes["text"])
  

def mensaje2():
    mes = random.choice(msgs2Tiro)
    print(mes["text"])
   
  
opciones_de_tiro = {
    "1w": mensaje1,
    "1d": mensaje1,
    "1a": mensaje1,
    "1s": mensaje1,
    "2w": mensaje2,
    "2d": mensaje2,
    "2a": mensaje2,
    "2s": mensaje2
}

def runMainFunccion():
    
    disparo = (input("introduce el numero de disparos(1o2) y la direccion(delante:w a la derecha:d a la izquierda:a detras:s): "))
      
    if disparo in opciones_de_tiro:
        opciones_de_tiro[disparo]()    
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