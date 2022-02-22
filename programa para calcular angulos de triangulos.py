import numpy as np
def angulotg(o,a):
    angulo=np.arctan(o/a)
    grados=angulo*(360/(2*np.pi))
    return(grados)
def angulosin(o,h):
    an=np.arcsin(o/h)
    grados=an*(360/(2*np.pi))
    return(grados)
def angulocos(a,h):
    an=np.arccos(a/h)
    grados=an*(360/(2*np.pi))
    return(grados)
o=input("ingrese funcion tg,cos,sen:")
if o == "tg":
    a=float(input("ingrese opuesto: "))
    b=float(input("ingrese adyacente:"))
    r=float(angulotg(a,b))
    print(round(r,2),"°")
if o == "cos":
        a1=float(input("ingrese adyacente: "))
        b1=float(input("ingrese hipotenusa:"))
        r1=angulocos(a1,b1)
        print(round(r1,2),"°")
elif o == "sen":
        a2=float(input("ingrese opuesto: "))
        b2=float(input("ingrese hipotenusa:"))
        r2=angulosin(a2,b2)
        print(round(r2,2),"°")
