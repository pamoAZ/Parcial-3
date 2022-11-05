#Importar librerias
from math import *
import numpy as np
from matplotlib import pyplot as plt
from sympy import integrate, sin, cos, E
from sympy.abc import x

#crear variables 

inf="Ingrese el límite de integración inferior:\n"
sup="Ingrese el límite de integración superior:\n"
subint="Ingrese un número impar positivo de subintervalos:\n"
numinv="El valor ingresado no es válido.\n"
functionmensage = "ingrese la funcion:\n"
res='El resultado aproximado es: '
fl="<string>"
fe="exec"


def datos():
  global a
  global b
  global fx
  global funcion
  global funcion1
  funcion = input(functionmensage)
  funcion1 = funcion.lower()

  fx= lambda x: eval(funcion1)

  #definir datos que se solicitan al usuario

  a=float(input(inf)) #limite inferior

  b=float(input(sup)) #limite superior

  n=int(input(subint)) #cantidad de subintervalos
  metodoAproximar(a,b,n,fx)



def metodoAproximar(a, b, n, fx):
  global integral
  # Condicionar el ingreso de n a impar positivo
  par=n%2
  while n<1 or par==0:
    n=int(input(subint))
    par=n%2

  # Desarrollo de la función
  h = (b-a)/n
  xi = a
  suma = fx(xi)
  for i in range(0,n-2,2):
    xi = xi + h
    suma = suma + 4*fx(xi)
    xi = xi + h
    suma = suma + 2*fx(xi)
  xi = xi + h
  suma = suma + 4*fx(xi)
  suma = suma + fx(b)
  integral = (h/3)*suma



def graficas(a,b,fx,funcion):

  m1= "Graficas de: {}"
  m2="V aproximado: "
  m3="V real: "
  xl="Eje x"
  yl="Eje y"
  x2l="x"
  y2l="y"
  c='g'
  c2='r'
 

  #ejes
  x1=np.array(range(int(a*10),int((b+0.1)*10)))*0.1
  y = list(map(fx,x1))

  #Grafica 1
  plt.subplot(211)
  plt.title(m1.format(funcion1))
  plt.xlabel(xl)
  plt.ylabel(yl)
  plt.plot(x1,y)
  plt.fill_between(x1,y,color=c)
  plt.legend([str(m2+str(integral))])

  #Grafica 2
  plt.subplot(212)
  plt.xlabel(x2l)
  plt.ylabel(y2l)
  plt.plot(x1,y)
  plt.fill_between(x1,y,color=c2)
  integralValorReal = integrate(funcion,(x,a,b))
  plt.legend([str(m3+str(integralValorReal))])

def main():
  datos()

  #Respuesta
  print(res, integral)

  graficas(a,b,fx,funcion)


main()