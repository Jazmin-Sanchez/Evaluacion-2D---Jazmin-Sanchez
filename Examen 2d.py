# Evaluacion-2D---Jazmin-Sanchez

# Examen de graficacion 2d sanchez canul jazmin yamilet.
# 14/12/2020 No. control = 18390058
import matplotlib.pyplot as plt
import numpy as np

plt.axis([-10,350,-10,300])
plt.axis('on')
plt.grid(True)
plt.title('Examen de graficación 2D Sanchez Jazmin')

#Primer rectangulo (Ultimos 3 digitos de mi numero de control = 058)
x1=0
x2=200
y1=160
y2=0

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(0,.5,.8))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(0,.5,.8))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(0,.5,.8))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(0,.5,.8))

#Primer rectangulo (Ultimos 3 digitos de mi numero de control = 058)
x1=100
x2=300
y1=240
y2=80

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(.5,0,.8))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(.5,0,.8))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(.5,0,.8))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(.5,0,.8))

#Circulo  (Ultimos 3 digitos de mi numero de control = 058)
xc=200
yc=160
r=40 #Radio

p1=0*np.pi/180
p2 =360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p) 
    plt.plot([xlast,xp],[ylast,yp], color= (.8,.5,0),linewidth=1)
    xlast=xp
    ylast=yp

plt.text(100,250, 'No. control = 18390058')
plt.text(230,200, 'Radio = 40')
plt.text(230,190, '8 * 5 = 40')

plt.show()
