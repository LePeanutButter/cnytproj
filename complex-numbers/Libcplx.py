import math

def sumaC(a=[], b=[]):
    real = a[0]+b[0]
    imaginario = a[1]+b[1]
    return (round(real,4), round(imaginario,4))

def restaC(a=[], b=[]):
    real = a[0]-b[0]
    imaginario = a[1]-b[1]
    return (round(real,4), round(imaginario,4))

def multiplicacionC(a=[], b=[]):
    real = a[0]*b[0] - a[1]*b[1]
    imaginario = a[0]*b[1] + b[0]*a[1]
    return (round(real,4), round(imaginario,4))

def divisionC(a=[], b=[]):
    denominador = (b[0]**2) + (b[1]**2)
    real = ((a[0]*b[0])+(a[1]*b[1]))/denominador
    imaginario = ((b[0]*a[1])-(a[0]*b[1]))/denominador
    return (round(real,4), round(imaginario,4))

def moduloC(a=[]):
    real = round(math.sqrt((a[0]**2)+(a[1]**2)), 4)
    return real

def conjugadoC(a=[]):
    return (a[0], -a[1])

def CVR(a=[], modelo=""):
    if modelo.lower()=="cartesiano":
        real = a[0] * math.cos(a[1])
        imaginario = a[0] * math.sin(a[1])
        return (round(real,4), round(imaginario,4))
    elif modelo.lower()=="polar":
        rho = moduloC(a)
        tetha = fase(a)
        return (rho, tetha)
    raise Exception("Solo se puede hacer conversiones polares o cartesiano")
    
def fase(a=[]):
    return round(math.atan(a[1]/a[0]), 4)

def prettyPrinting(real, imaginario):
    if imaginario < 0:    
        return f"{real}{imaginario}i"
    return f"{real}+{imaginario}i"