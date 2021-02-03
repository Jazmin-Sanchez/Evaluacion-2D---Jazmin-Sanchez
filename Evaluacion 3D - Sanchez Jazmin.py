# Evaluacion-3D---Jazmin-Sanchez
# Examen de graficacion 3D sanchez canul jazmin yamilet.
# 03/02/2020 No. control = 18390058
# Utilizo los ultimos 3 digitos de mi numero de control como colores
# Uso de la libreria keyboard (pip install keyboard)

import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import keyboard



def ploteoFigura(x,y,z):
    plt.axis([0,150,120,0])
    plt.axis('on')
    plt.grid(True)
    plt.title("'Evaluacion de recuperación 3D'")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")



    #___Ploteo triangulo base
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
    plt.text(60,65,'A',color=(0,.5,.8))
    plt.text(x[3]-10,y[3],'A1',color=(.8,0,.5))
    plt.text(x[3]-5,y[3]+10,'A2',color=(.5,0,.8))

    #____Hitpoint
    plt.scatter(x[3],y[3],s=20,color='r')

    #____Trazo de los triangulos
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color=(0,.5,.8)) 
    plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color=(.8,0,.5))
    plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color=(.5,0,.8))


    #——Etiqueta de las esquinas
    plt.text(25,10,'1')
    plt.text(83,63,'2')
    plt.text(x[3]+2,y[3],'3')

    #——Calcular perimetro Triangulo A (lado a,b,c)(0,1y2)
    abA=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    acB=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    bcC=sqrt(((x[2]-x[1])*(x[2]-x[1])) + ((y[2]-y[1])*(y[2]-y[1])))
    #__Calculo del perimetro, semiperimetro y Area A
    #(Formula de Heron) area= sqrt(s(s-a)(s-b)(s-c))

    pA = abA+acB+bcC
    spA = pA/2
    AreaA= sqrt((spA*(spA-abA)*(spA-acB)*(spA-bcC)))

    plt.text(100,40,'A=',color=(0,.5,.8))
    dle='%7.0f'% (AreaA)
    dls=str(dle)
    plt.text(105,40,dls)

    #——Calcular perimetro Triangulo A1 (lado a,b,c) (0,1y3)
    abA1=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    acB1=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    bcC1=sqrt(((x[3]-x[1])*(x[3]-x[1])) + ((y[3]-y[1])*(y[3]-y[1])))

    #__Calculo del perimetro, semiperimetro y Area A1
    #(Formula de Heron) area= sqrt(s(s-a)(s-b)(s-c))
    pA1 = abA1+acB1+bcC1
    spA1 = pA1/2
    AreaA1= sqrt((spA1*(spA1-abA1)*(spA1-acB1)*(spA1-bcC1)))

    plt.text(100,45,'A1=',color=(.8,0,.5))
    dle='%7.0f'% (AreaA1)
    dls=str(dle)
    plt.text(105,45,dls)

    #——Calcular perimetro Triangulo A2 (lado a,b,c)(0,3y2)
    abA2=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    acB2=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    bcC2=sqrt(((x[3]-x[2])*(x[3]-x[2])) + ((y[3]-y[2])*(y[3]-y[2])))

    #__Calculo del perimetro, semiperimetro y Area A2
    #(Formula de Heron) area= sqrt(s(s-a)(s-b)(s-c))
    pA2 = abA2+acB2+bcC2
    spA2 = pA2/2
    AreaA2= sqrt((spA2*(spA2-abA2)*(spA2-acB2)*(spA2-bcC2)))

    plt.text(100,50,'A2=',color=(.5,0,.8)) 
    dle='%7.0f'% (AreaA2)
    dls=str(dle)
    plt.text(105,50,dls)

    #____Se suman las areas A1 y  A2
    #para determina si el hitpoint está afuera o dentro del limite
    areaSuma=AreaA1+AreaA2
    plt.text(100,55,'A1+A2=',color=(0,.8,.5)) 
    dle='%7.0f'% (areaSuma)
    dls=str(dle)
    plt.text(120,55,dls)
    if(areaSuma<AreaA):
        plt.text(40,90,'El HitPoint se encuentra dentro de los limites c:')
    else:
        plt.text(40,90,'El Hitpoint se encuentra fuera de los limites :c')

    plt.show()

print("Ingrese Enter para continuar, para terminar proceso presione Esc")
while True:

    if keyboard.is_pressed('ENTER'):
        input()    
        #____Pedir puntos de las coordenadas x y y del hitpoint
        pntx = float(input('ingresa la coordena x del hitpoint ='))
        pnty = float(input('ingresa la coordena y del hitpoint ='))
        #___Plano
        x=[40,30,80,pntx] 
        y=[60,10,60,pnty]
        z=[0,0,0,0]

        ploteoFigura(x,y,z)

    if keyboard.is_pressed('Esc'):
        print("Fin de la ejecucion uwu")
        break

    
