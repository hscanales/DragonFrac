
###Importando librerias#######
import tkinter.messagebox
from math import*
from tkinter import*
from tkinter import ttk
import tkinter
import time
import random
from tkinter import font


#################################VENTANA 1##################################

#Definiendo funcion nickname
def iniciar_juego(nickname,ventana,ventana_juego):
#validacion de nickname vacio
    if(nickname!=""):
        #Validacion de nickname alfabetico o numerico
        if(nickname.isalnum()):
            #Validando que el nickname tenga cierta cantidad de letras
            if(len(nickname)>=5 and len(nickname)<=8):
                tkinter.messagebox.showinfo("Bienvenido",nickname)
                #Llama la funcion de tiempo, para que se inicie 
                tiempo()
                #ocultando ventana principal
                ventana.withdraw()
                tutos.withdraw()
                #mostrando segunda ventana
                ventana_juego.deiconify()
            else:tkinter.messagebox.showerror("No se puede iniciar","Ingrese un Nickname de 5 a 8 letras o numeros")
#Mostrando errores
        else:tkinter.messagebox.showerror("No se puede iniciar","Ingrese un Nickname sin caracteres especiales")
    else:tkinter.messagebox.showerror("No se puede iniciar","Ingrese un Nickname")


#Aceptar el ingrese de enter
def callback(event):
    iniciar_juego(variable_nickname.get(),root,ventana_juego)

#Creando y configurando ventana principal
root=Tk()
root.geometry("510x350")
root.title("Dragon Frac")
root.resizable(width=False, height=False)
img=PhotoImage(file="logo.png")
widget=Label(root,image=img).pack()
#creando contenedor
contenedor = Frame(root, width=200, height=150).place(x=300,y=185)
lblNickname = Label(contenedor, text="NickName:")
lblNickname.pack()
lblNickname.place(x=350,y=225)
variable_nickname = StringVar()
#Creando espacio para ingresar Nickname
txtNickname = Entry(contenedor, textvariable=variable_nickname)
txtNickname.pack()
txtNickname.place(x=350,y=250)
txtNickname.bind("<Return>",callback)
#creando boton de inicio de juego
btnIniciar = Button(contenedor, text="Iniciar", width=10,height=2, command=lambda:iniciar_juego(variable_nickname.get(),root,ventana_juego))
btnIniciar.pack()
btnIniciar.place(x=350,y=275)
    
###########################CREANDO SEGUNDA VENTANA#####################
#definiendo dimensiones de segunda ventana
ventana_juego = Toplevel(root)
ventana_juego.geometry("=900x600")
ventana_juego.resizable(width=False, height=False)
#creando lbl de tiempo en segunda ventana
lbltiempo=Label(ventana_juego,text="",font=font.Font(size=20))
lbltiempo.pack()
#definiendo widget de tiempo en segunda ventana
lblPuntaje = Label(ventana_juego,text="Puntaje:",font=font.Font(size=20))
lblPuntaje.place(x=20, y=5)
Puntaje = Label(ventana_juego, text="0", font=font.Font(size=20))
Puntaje.place(x=125, y=5)


#Definiendo y creando canvas de segunda ventana
lienzo=Canvas(ventana_juego, width=900,height=600, bg="black" )
lienzo.pack()
#Variables globales para el fractal
x=450
y=475
a=x-15
b=y-4.5
c=x+43
d=y+53.5
xy = []
Puntajecoor = []
acumP = 0
e=a+10
f=b+10
#Creando funcion de rango de replica para el fractar
def Distancia(x1, y1, x2, y2):
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    if (60< d <90):
        return True
    return False
#Defininedo tamaño, del circulo replicado.
def Diferencia(C1, C2):
    print(C1, C2)
    if (C1 <= C2):
        return C2-C1
    else:
        return C1-C2        
#Definicion de funcion para sumar puntaje
def SumPuntaje(coordenadas):
    global Puntajecoor, acumP
    for i in Puntajecoor:
        if (i[1]==coordenadas):
            acumP = acumP+i[0] #Si cumple la condicion, se acumula los puntos obtenidos, se colocan en la pantalla de juego y se retorna el total acumulado
            Puntaje["text"] = acumP 
            lblPuntaje2["text"]=acumP 
            return acumP
    
#Definicion funcion para Borrar Burbujas
def BurbujaDelete(x, y): 
    global xy
    print(xy)
    for coordenadas in xy:
        #se serciora que ambas coordenandas esten a una distancia menor que el diametro de las burbujas
            if(Diferencia(x, coordenadas[0])<= 40):
                if(Diferencia(y, coordenadas[1])<= 40):
                    #"Elimina" las burbujas creando una burbuja con el color de fondo de el canvas encima de esta
                    lienzo.create_oval(coordenadas, fill= "black", outline= "black")
                    SumPuntaje(coordenadas)
                    xy.remove(coordenadas)
                    if (len(xy)==0):
                        ventana_juego.withdraw()
                        ventana_puntaje.deiconify()
#Definicion funcion para replicar el fractal
def callback(event):
    global x,y,a,b,c,d
    if(Distancia(x, y, event.x, event.y)):
        x = event.x
        y = event.y
        e=x-30
        f=y-7
        g=x+87
        h=y+107
        a=e
        b=f
        c=g
        d=h
        BurbujaDelete(x, y)
        circulo()
        copo(2)
#Definiendo el copo y su nivel de recursividad
def copo(n):

    x_ver1=x
    y_ver1=y
    x_ver2=x
    y_ver2=y+100
    x_ver3=x+87
    y_ver3=y+50

    curva(x_ver1,y_ver1,x_ver2,y_ver2,n+1)
    curva(x_ver2,y_ver2,x_ver3,y_ver3,n+1)
    curva(x_ver3,y_ver3,x_ver1,y_ver1,n+1)
    curva(x_ver1,y_ver1,x_ver2,y_ver2,n+1)
    return

#Definiendo la curva de cada linea del copo
def curva(xi,yi,xf,yf,n):
    if n==0:
        lienzo.create_line(xi,yi,xf,yf,fill="Black")

    elif n>0:
        x1=xi+(xf-xi)/3
        y1=yi+(yf-yi)/3

        x3=(2*xf+xi)/3
        y3=(2*yf+yi)/3

        x2=x1+(x3-x1)*cos(pi/4)-(y3-y1)*sin(pi/4)
        y2=y1+(y3-y1)*cos(pi/4)+(x3-x1)*sin(pi/4)

        curva(xi,yi,x1,y1,n-1)
        curva(x1,y1,x2,y2,n-1)
        curva(x2,y2,x3,y3,n-1)
        curva(x3,y3,xf,yf,n-1)
        return
#Circulo de fractal original
def circulo():
     lienzo.create_oval(a,b,c,d,fill="white")
     return
def canvasborrar():
    lienzo.delete("all")

#################### Definiendo la creacion de las burbujas######################
ColoresyPuntaje={"green":100, "yellow":200,"red":500}

#Se crea una tupla que dara el color de las burbujas
Llavecolor=("green","yellow","red")
#funcion para crear la burbuja
def burbujas():
    global xy
    num=0
    while(num<9):
        xa=random.randint(10,850)
        ya=random.randint(10,300)

        if (lienzo.find_overlapping(xa,ya,xa+40,ya+40)==()):
            Txy = xa, ya, xa+40, ya+40
            xy.append(Txy)
            color = random.sample(Llavecolor,1)
            Puntajecoor.append([ColoresyPuntaje[color[0]], Txy])
            lienzo.create_oval(xa,ya,xa+40,ya+40,fill=color,outline=color)
            num = num + 1
#########funcion de cuenta regresiva#########

seg=60 #Se define la cantidad maxima de tiempo.
def tiempo(): 
    global seg
    #Es utilizado para que el tiempo salga en la pantalla
    lbltiempo["text"]=seg 
    #Se hace que el tiempo vaya en cuenta regresiva
    seg = seg -1 
    i=lbltiempo.after(1000,tiempo)  
    if (seg==-1):
        lbltiempo.after_cancel(i)
        #si se acaba el tiempo, ocultar la ventana 2
        ventana_juego.withdraw()
        #y mostrar la de puntaje
        ventana_puntaje.deiconify()

#####Ventana Tutos###
#Se define y se configura la ventana para el tutorial
tutos=Toplevel(root)
alturat=600
anchot=400
anchop=root.winfo_screenwidth()
alturap=root.winfo_screenheight()
xt=(anchop/3)+300
yt=(alturap/3)-250
tutos.geometry('%dx%d+%d+%d' % (anchot, alturat, xt, yt))
tutos.resizable(0,0)
#Se carga el archivo donde estan las instrucciones
imgtutos=PhotoImage(file="tuto.png")
tutoimg=Label(tutos,image=imgtutos).pack()


def easteregg():
    global imgea,anchop,alturap, acumP
    huevo=Toplevel(ventana_juego)
    alturae=550
    anchoe=504
    xe=(anchop/4)
    ye=(alturap/4)
    huevo.geometry('%dx%d+%d+%d' % (anchoe, alturae, xe, ye))
    huevo.resizable(0,0)
    imgea=PhotoImage(file="fondo2.png")
    huevoimg=Label(huevo,image=imgea).pack()
#########################Creando menu###########################
barraMenu=Menu(ventana_juego)
#crear los menus
menu=Menu(barraMenu)
#crear los comandos de los menus
menu.add_command(label="Easter Egg", command=lambda:easteregg())
menu.add_command(label="Terminar", command=exit)
#Agregar los menus a la barra de Menus
barraMenu.add_cascade(label="Opciones",menu=menu)

#Indicamos que la barra de menús estara en la ventana
ventana_juego.config(menu=barraMenu)

##########################Creando ventana de puntaje##########################

#Creando la ventana
ventana_puntaje=Toplevel(ventana_juego)
#titulo de la ventana
ventana_puntaje.title("Puntaje Final")
#Asigna un tamaño a la ventana
ventana_puntaje.geometry("510x350")
#Hace que la ventana no se pueda cambiar de tamaño
ventana_puntaje.resizable(width=False, height=False)
#Comando que cuando se cierre la ventana de puntaje, se cierre la principal 
ventana_puntaje.protocol("WM_DELETE_WINDOW",root.destroy)
#Poniendo fondo de ventana final
im=PhotoImage(file="fondo.png")
wid=Label(ventana_puntaje,image=im).pack()
#Contenedor Frame que se utiliza para ordenar los componentes (cuadro de texto, label)
contenedorde_puntaje = Frame(ventana_puntaje, width=200, height=200, bg="grey")
contenedorde_puntaje.pack()
contenedorde_puntaje.place(x=135, y=100)
#Etiqueta puntaje.
lblPuntajeNickName = Label(contenedorde_puntaje, text="Puntaje final", bg="grey", font=font.Font(family="Helvetica", size=20))
lblPuntajeNickName.pack(padx=40, pady=20)
#PuntajeU = Label(
#Almacenador de puntaje
lblPuntaje2 = Label(contenedorde_puntaje, bg="white", font=font.Font( size=14))
lblPuntaje2.pack(padx=40)
#boton para cerrar el juego
btncerrar= Button(ventana_puntaje, text="Cerrar", width=10,height=2, command=exit)
btncerrar.pack()
btncerrar.place(x=300,y=250)
ventana_puntaje.withdraw()

##########################################################################
##MAIN##

#Se inician todas las fnciones necesarias para el juego
burbujas()
circulo()
copo(3)
lienzo.bind('<Button-1>',callback)
ventana_juego.withdraw()



#Codigo elaborado en conjunto por: David Alejandro Guardado Chinchilla, Héctor Sául Canales.


