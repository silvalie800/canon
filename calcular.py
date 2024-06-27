o1=int(input("introduce un numero: "))
calculadora=(input("intoduce + - * /: "))
o2=int(input("introduce otro numero: "))
result=0

if calculadora == "+":
    result = o1+o2
elif calculadora == "-":
    result = o1-o2
elif calculadora == "*":
    result = o1*o2
elif calculadora == "/":
    result = o1/o2
else:
    print("introduce una de las opciones")

print(result)   

