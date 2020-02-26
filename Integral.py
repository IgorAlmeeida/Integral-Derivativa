from Derivada import *

def derivar(fun,x):
    e = 0.000000001
    return (fun(x+e) - fun(x))/e        

def pontos(func, x0, x1, qttReta):
    lista = []
    aux = (x1 - x0)/qttReta
    for i in range (qttRetas):
        if (i == 0):
            lista.append(x0)
        elif (i == qttRetas -1):
            lista.append(x1)
        else:
            lista.append(lista[i-1] + aux)
    return (lista)

def intersec(func,listaPontos):
    lista = []
    lista.append(listaPontos[0])
    for i in range (len(listaPontos)-1):
        x0 = listaPontos[i]
        x1 = listaPontos[i+1]
        m0 = derivar(func,x0)
        m1 = derivar(func,x1)
        funX0 = func(x0)
        funX1 = func(x1)
        x = ((-m1*x1)+(m0*x0) + (funX1) - (funX0))/(m0 - m1)
        lista.append(x)
    lista.append(listaPontos[len(listaPontos)-1])
    return lista

def integral (func, pontos0, pontos1):
    area = 0
    for i in range(len(pontos1)-1):
        m0 = derivar(func,pontos1[i])
        x0 = pontos1[i]
        x1 = pontos1[i+1]
        funX0 = (m0*x0) - (m0*pontos0[i]) + func(pontos0[i])
        funX1 = (m0*x1) - (m0*pontos0[i]) + func(pontos0[i])
        area += (((x1 - x0) * (funX1 - funX0))/2)
        if (funX0 > funX1):
            area += funX1 *(x1 - x0)
        else:
            area += funX0 *(x1 - x0)
    print (area)
    print ("")
    

def integracaoDerivada(func, x0, x1, qttRetas):
    interseao = pontos (func, x0, x1, qttRetas)
    pontos1 = intersec(func, interseao)
    integral(func, interseao, pontos1)


while (True):
    func = lambda x: x**2 + 1
    print("Integral")
    x0 = int(input("X0:"))
    x1 = int(input("X1:"))
    qttRetas = int(input("Número de Retas:"))
    integracaoDerivada(func, x0, x1, qttRetas)


