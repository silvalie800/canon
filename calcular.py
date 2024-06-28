def run_main_funccion():

 n1=(input("introduce un numero: "))
 calculadora=(input("intoduce + - * /: "))
 n2=(input("introduce otro numero: "))
 result=0

 if calculadora == "+":
    result =int(n1+n2)
 elif calculadora == "-":
    result =int(n1-n2)
 elif calculadora == "*":
    result =int(n1*n2)
 elif calculadora == "/":
    result =int(n1/n2)
 else:
    print("introduce una de las opciones")
 
 print(result)   

def checkExit():
    resp = ""

    while (resp != "n" and resp != "s"):
        resp = input("quieres seguir calculando? [s/n]")
        if resp == "n" : 
            return False
    return True

running = True
while running :
    run_main_funccion()
    running = checkExit()