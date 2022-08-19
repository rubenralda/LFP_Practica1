from operator import le
from tkinter.messagebox import showerror, showinfo
from PyQt5 import QtWidgets, uic, QtCore
from tkinter import *
from tkinter import filedialog
from PyQt5.QtWidgets import QMessageBox, QFileDialog


app = QtWidgets.QApplication([])
cursos=[]

# Cargar Ventanas
menuPrincipal = uic.loadUi("menuPrincipal.ui")
cargarArchivo = uic.loadUi("cargarArchivo.ui")
gestionCursos = uic.loadUi("gestionarCursosMenu.ui")

listaCursos=uic.loadUi("listaCursos.ui")
buscarCurso=uic.loadUi("buscarCurso.ui")

# Funciones
def botonCargarArchivo():
    menuPrincipal.hide()
    cargarArchivo.show()


def regresarPrincipal():
    menuPrincipal.show()
    cargarArchivo.hide()


def buscarArchivo():
    filetypes = (
        ('text files', '*.lfp'),
        ('All files', '*.*')
    )
    f = filedialog.askopenfilename(
        initialdir="/", title="Escoge el Archivo", filetypes=filetypes)
    cargarArchivo.txtRuta.setText(f)

def cargarFile():
    if cargarArchivo.txtRuta.text()!="":
        try:
            file = open(cargarArchivo.txtRuta.text(),"r+")
            cursos.clear()
            for linea in file:
                cursos.append(linea.replace("\n","").split(","))
            file.close()
        except:
            showerror("Error", "Error al cargar el archivo")  
        showinfo("Información","El archivo fue cargado con exito")
        validar()
        cargarArchivo.hide()
        menuPrincipal.show()
    else:
        showerror("Error", "Ingrese una ruta")

def validar():
    for codigo in cursos:
        repitencia,i=0,0
        while i<len(cursos):
            if cursos[i][0]==codigo[0]:
                repitencia+=1
                if repitencia==1:
                    borrar=i
            if repitencia>1:
                cursos.pop(borrar)
                borrar=i-1
                repitencia-=1
            i+=1     

def buttonGesCursos():
    gestionCursos.show()
    menuPrincipal.hide()
def buttonRegresar2():
    menuPrincipal.show()
    gestionCursos.hide()

def buttonLista():
    listaCursos.show()
    gestionCursos.hide()

def buttonRegresarLista():
    gestionCursos.show()
    listaCursos.hide()
    
def buttonBuscar():
    buscarCurso.show()
    gestionCursos.hide()

def buttonRegresarLista2():
    gestionCursos.show()
    buscarCurso.hide()

def buttonCargar():
    if cursos==[]:
        showerror("Error", "Cargue un archivo")
    else:
        m=len(cursos)
        listaCursos.tableWidget.setRowCount(m)
        tableRow=0
        for curso in cursos:
            listaCursos.tableWidget.setItem(tableRow,0,QtWidgets.QTableWidgetItem(curso[0]))
            listaCursos.tableWidget.setItem(tableRow,1,QtWidgets.QTableWidgetItem(curso[1]))
            listaCursos.tableWidget.setItem(tableRow,2,QtWidgets.QTableWidgetItem(curso[2]))
            listaCursos.tableWidget.setItem(tableRow,3,QtWidgets.QTableWidgetItem(curso[3]))
            listaCursos.tableWidget.setItem(tableRow,4,QtWidgets.QTableWidgetItem(curso[4]))
            listaCursos.tableWidget.setItem(tableRow,5,QtWidgets.QTableWidgetItem(curso[5]))
            listaCursos.tableWidget.setItem(tableRow,6,QtWidgets.QTableWidgetItem(curso[6]))
            tableRow+=1

def buscar():
    encontrado=False
    if buscarCurso.txtCodigo.text()!="":
        for curso in cursos:
            if buscarCurso.txtCodigo.text()==curso[0]:
                encontrado=True
                obligatorio= 'obligatorio' if int(curso[3]) == 0 else 'opcional'
                if int(curso[6])==0:
                    estado="Aprobado"
                elif int(curso[6])==1:
                    estado="Cursando"
                elif int(curso[6])==-1:
                    estado="Pendiente"
                buscarCurso.curso.setText(f"Nombre: {curso[1]}, es {obligatorio}\nSemestre: {curso[4]} \nCréditos: {curso[5]}\nEstado: {estado}")
                break
        if encontrado==False:
            showerror("Error", "El código no existe")
    else:
        showerror("Error", "Ingrese el código")
# Agregar Eventos

menuPrincipal.buttonCargar.clicked.connect(botonCargarArchivo)
menuPrincipal.buttonSalir.clicked.connect(exit)
menuPrincipal.buttonCursos.clicked.connect(buttonGesCursos)

cargarArchivo.buttonRegresar.clicked.connect(regresarPrincipal)
cargarArchivo.buttonSelect.clicked.connect(buscarArchivo)
cargarArchivo.buttonCargar.clicked.connect(cargarFile)

gestionCursos.buttonRegresar.clicked.connect(buttonRegresar2)
gestionCursos.buttonLista.clicked.connect(buttonLista)
gestionCursos.buttonBuscar.clicked.connect(buttonBuscar)

listaCursos.buttonRegresar.clicked.connect(buttonRegresarLista)
listaCursos.buttonCargar.clicked.connect(buttonCargar)

buscarCurso.buttonRegresar.clicked.connect(buttonRegresarLista2)
buscarCurso.buttonBuscar.clicked.connect(buscar)
# Iniciar aplicacion
menuPrincipal.show()
app.exec()