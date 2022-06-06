
#Tarea 7 y 8
#"escriba un programa en python que permita llevar un control de presupuesto de un proyecto, cada rubro del proyecto debe llevar el código del control de costos, una descripción, monto presupuesto, monto ejecutado
#Su programa debe permitir guardar la información del proyecto en un archivo txt con el nombre del proyecto.
#Además se debe poder
#1.abrir un proyecto
#2.crear un proyecto
#3.agregar un nuevo rubro a un proyecto ya existente
#4. Reportar un gasto sobre un rubro existente
#5.generar un gráfico por porcentaje por rubro
#6. Generar un gráfico Por ejecución de presupuesto
#7. Salir

import matplotlib.pyplot as plt
import numpy as np


nombre_proyecto = ''
rubros = [] 
class Rubro:

    def __init__(self, codigo_control, descripcion,monto_presupuestado, monto_ejecutado = 0):
        self.codigo_control = codigo_control
        self.descripcion = descripcion
        self.monto_presupuestado = monto_presupuestado
        self.monto_ejecutado = monto_ejecutado
        
    
    def agregar_gasto(self, monto):
        self.monto_ejecutado += monto


    def to_string(self):
        return  self.codigo_control + "," + self.descripcion + "," + str(self.monto_presupuestado) + "," + str(self.monto_ejecutado) + '\n'

    
    @staticmethod
    def from_string(string):
        datos = string.split(",")
        rubro = Rubro(datos[0],datos[1],int(datos[2]), int(datos[3]))
        return rubro

def leer_proyecto( nombre):
    global nombre_proyecto
    nombre_proyecto = nombre
    f = open (nombre + '.txt','r')
    datos = f.read()
    f.close()
    rub = datos.split('\n')
    for r in rub:
        if(r != ''):
            rubros.append(Rubro.from_string(r))

def guardar_proyecto():
    ruta = nombre_proyecto + ".txt"
    datos = ''
    for rubro in rubros:
        datos += rubro.to_string()
    f = open (ruta,'w')
    f.write(datos)
    f.close()


def crear_proyecto(nombre):
    global rubros
    global nombre_proyecto
    rubros = []
    nombre_proyecto = nombre
    guardar_proyecto()

def agregar_rubro(rubro):
    for r in rubros:
        if(r.codigo_control == rubro.codigo_control):
            return False

    rubros.append(rubro)
    guardar_proyecto()
    return True    

def reportar_gasto(codigo_control, monto_gasto):
    for r in rubros:
        if(r.codigo_control == codigo_control):
            r.agregar_gasto(monto_gasto)
            guardar_proyecto()

def menu_abrir_proyecto():
    print('Ingrese el nombre del proyecto')
    dir = input()
    leer_proyecto(dir)
    print('Proyecto cargado exitosamente')

def menu_crear_proyecto():
    print(nombre_proyecto)
    if(nombre_proyecto != ''):
        print('Existe un proyecto abierto. ¿desea guardarlo?')
        print('(s/n)')
        opcion = input()
        if opcion == 's':
            guardar_proyecto('')
    print('Ingrese el nombre del proyecto')
    proyecto = input()
    crear_proyecto(proyecto)
    print('Proyecto creado exitosamente')

def menu_agregar_rubro():
    print('Ingrese el código de control')
    cod = input()
    print('Ingrese una descripción')
    desc = input()
    print('Ingrese el presupuesto')
    presupuesto = int(input())
    rubro = Rubro(cod,desc,presupuesto)
    agregar_rubro(rubro)
    print("Rubro agregado exitosamente")

def menu_reportar_gastos():
    print("Ingrese el código de control")
    cod = input()
    print('ingrese el monto gastado')
    monto = int(input())
    for r in rubros:
        if(r.codigo_control == cod):
            r.agregar_gasto(monto)
            guardar_proyecto()
            return
    print("Rubro no encontrado")

def generar_grafico_rubro():
    presupuesto_total = 0
    for rubro in rubros:
        presupuesto_total += rubro.monto_presupuestado

    labels = []
    sizes = []
    for rubro in rubros:
        labels.append(rubro.codigo_control)
        sizes.append(rubro.monto_presupuestado * 100 / presupuesto_total)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def generar_grafico_Ejecucion():
    np.random.seed(3)
    x = []
    y = []
    for rubro in rubros:
        x.append(rubro.codigo_control)
        y.append(rubro.monto_ejecutado * 100 / rubro.monto_presupuestado)
    
    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(-1, 8), xticks=np.arange(0, 8),
        ylim=(0, 100), yticks=np.arange(0, 10)* 10)
    plt.title("Porcentaje de ejecución por rubros")
    plt.show()

def menu_principal():
    runing = True
    while(runing):
        print('SISTEMA DE GESTIÓN DE GASTOS')
        print('----------------------------')
        print('1- ABRIR PROYECTO')
        print('2- CREAR PROYECTO')
        print('3- AGREGAR UN NUEVO RUBRO')
        print('4- REPORTAR GASTO')
        print('5- GENERAR GRAFICO POR RUBRO')
        print('6- GENERAR GRAFICO POR EJECUCION DEL PRESUPUESTO')
        print('7- SALIR')
        print('----------------------------')
        print('INGRESE LA OPCIÓN QUE NECESITA')
        opcion = input()
        if(opcion == '1'):
            menu_abrir_proyecto()
        elif(opcion == '2'):
                menu_crear_proyecto()
        elif(opcion == '3'):
                menu_agregar_rubro()
        elif(opcion == '4'):
                menu_reportar_gastos()
        elif(opcion == '5'):
                generar_grafico_rubro()
        elif(opcion == '6'):
            generar_grafico_Ejecucion()
        elif(opcion == "7"):
            runing = False


menu_principal()