# Practicas2021
# extra
## Como extra puede agregar un Mbox para pedir al usuario que ingrese lo valores de a y b, determinado la amplitud de la elipse: 
    valores = mbox('Ingrese valores de a y b',entry="50,100")     
    a,b = [float(x.replace(' ','')) for x in valores.split(',')] 
