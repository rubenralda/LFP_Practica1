from tkinter.messagebox import showerror, showinfo
from PyQt5 import QtWidgets, uic
from tkinter import *
from tkinter import filedialog


app = QtWidgets.QApplication([])
cursos=[]

# Cargar Ventanas
menuPrincipal = uic.loadUi("ui/menuPrincipal.ui")
cargarArchivo = uic.loadUi("ui/cargarArchivo.ui")
gestionCursos = uic.loadUi("ui/gestionarCursosMenu.ui")
conteoCreditos = uic.loadUi("ui/conteoCreditos.ui")

listaCursos=uic.loadUi("ui/listaCursos.ui")
buscarCurso=uic.loadUi("ui/buscarCurso.ui")
agregarCurso=uic.loadUi("ui/agregarCurso.ui")
editarCurso=uic.loadUi("ui/editarCurso.ui")
eliminarCurso=uic.loadUi("ui/eliminarCurso.ui")

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
            file = open(cargarArchivo.txtRuta.text(),"r+",encoding="utf-8")
            cursos.clear()
            for linea in file:
                cursos.append(linea.replace("\n","").split(","))
            file.close()
            showinfo("Información","El archivo fue cargado con exito")
            validar()
            cargarArchivo.hide()
            menuPrincipal.show()
        except:
            showerror("Error", "Error al cargar el archivo")  
        
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

def buttonRegresarLista():
    gestionCursos.show()
    listaCursos.hide()
    
def buttonBuscar():
    buscarCurso.show()
    gestionCursos.hide()

def buttonRegresarLista2():
    gestionCursos.show()
    buscarCurso.hide()

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

def buttonAbrirAgregar():
    gestionCursos.hide()
    agregarCurso.show()

def buttonRegresarLista3():
    gestionCursos.show()
    agregarCurso.hide()

def buttonAbrirEditar():
    gestionCursos.hide()
    editarCurso.show()
    editarCurso.buttonEditar.setEnabled(False)
    editarCurso.buttonBuscar.setEnabled(True)
    editarCurso.buttonRegresar.setEnabled(True)

def buttonRegresarLista4():
    gestionCursos.show()
    editarCurso.hide()
    
def buttonAgregar():
    if agregarCurso.txtCodigo.text()=="":
        showerror("Error", "Ingrese un codigo")
    else:
        encontrado=False
        for curso in cursos:
            if agregarCurso.txtCodigo.text()==curso[0]:
                showerror("Error", "El codigo del curso ya existe")
                agregarCurso.txtCodigo.setText("")
                encontrado=True
                break
        if encontrado==False:
            if agregarCurso.txtNombre.text()!="" and agregarCurso.txtSemestre.text()!="" and agregarCurso.txtOpcion.text()!="" and agregarCurso.txtCreditos.text()!="" and agregarCurso.txtEstado.text()!="":
                cursos.append([agregarCurso.txtCodigo.text(),agregarCurso.txtNombre.text(),agregarCurso.txtRequisito.text(),agregarCurso.txtOpcion.text(),agregarCurso.txtSemestre.text(),agregarCurso.txtCreditos.text(),agregarCurso.txtEstado.text()])
                showinfo("Información","El curso se agregó exitosamente")
            else:
                showerror("Error", "Algunos campos son obligatorios")

u=0
def buttonBuscar2():
    if editarCurso.txtCodigo.text()=="":
        showerror("Error", "Ingrese un codigo")
    else:
        i=0
        existe=False
        for curso in cursos:
            if editarCurso.txtCodigo.text()==curso[0]:
                editarCurso.txtNombre.setText(curso[1])
                editarCurso.txtRequisito.setText(curso[2])
                editarCurso.txtSemestre.setText(curso[4])
                editarCurso.txtOpcion.setText(curso[3])
                editarCurso.txtCreditos.setText(curso[5])
                editarCurso.txtEstado.setText(curso[6])
                editarCurso.buttonEditar.setEnabled(True)
                editarCurso.buttonRegresar.setEnabled(False)
                editarCurso.buttonBuscar.setEnabled(False)
                cursos.pop(i)
                existe=True
                break
            i+=1
        if existe==True:
            showinfo("Información","Se ha cargado la informacion del curso")
        else:
            showinfo("Información","El curso no existe")


def buttonEditar():
    if editarCurso.txtNombre.text()!="" and editarCurso.txtSemestre.text()!="" and editarCurso.txtOpcion.text()!="" and editarCurso.txtCreditos.text()!="" and editarCurso.txtEstado.text()!="":
        cursos.append([editarCurso.txtCodigo.text(),editarCurso.txtNombre.text(),editarCurso.txtRequisito.text(),editarCurso.txtOpcion.text(),editarCurso.txtSemestre.text(),editarCurso.txtCreditos.text(),editarCurso.txtEstado.text()])
        showinfo("Información","El curso se ha editado exitosamente")
        editarCurso.buttonEditar.setEnabled(False)
        editarCurso.buttonRegresar.setEnabled(True)
        editarCurso.buttonBuscar.setEnabled(True)
    else:
        showerror("Error", "Algunos campos son obligatorios")

def buttonAbrirEliminar():
    eliminarCurso.show()
    gestionCursos.hide()

def buttonRegresarLista5():
    eliminarCurso.hide()
    gestionCursos.show()

def buttonEliminar():
    if eliminarCurso.txtCodigo.text()=="":
        showerror("Error", "Ingrese un codigo")
    else:
        i=0
        existe=False
        for curso in cursos:
            if eliminarCurso.txtCodigo.text()==curso[0]:
                cursos.pop(i)
                showinfo("Información","El curso se ha eliminado")
                existe=True
                break
            i+=1
        if existe==False:
            showerror("Error","El curso no existe")

def buttonAbrirConteo():
    conteoCreditos.show()
    menuPrincipal.hide()
    conteoaprobados=0
    conteocursando=0
    conteopendientes=0
    for curso in cursos:
        if int(curso[6])==0:#aprobado
            conteoaprobados+=int(curso[5])
        if int(curso[6])==1:#cursando
            conteocursando+=int(curso[5])
        if int(curso[6])==-1:#pendientes
            if int(curso[3])==1:#obligatorios
                conteopendientes+=int(curso[5])
    conteoCreditos.aprobados.setText("Créditos Aprobados: "+str(conteoaprobados))
    conteoCreditos.cursados.setText("Créditos Cursando: "+str(conteocursando))
    conteoCreditos.pendientes.setText("Créditos Pendientes: "+str(conteopendientes))

def buttonContar1():
    conteo=0
    if conteoCreditos.spinBox1.value()>0:
        for curso in cursos:
            if int(curso[4])<=conteoCreditos.spinBox1.value():
                if int(curso[3])==1:
                    conteo+=int(curso[5])
    conteoCreditos.txtObli.setText(str(conteo))

def buttonContar2():
    conteo=0
    if conteoCreditos.spinBox2.value()>0:
        for curso in cursos:
            if int(curso[4])==conteoCreditos.spinBox2.value():
                conteo+=int(curso[5])
    conteoCreditos.txtTotal.setText(str(conteo))

def buttonRegresar3():
    menuPrincipal.show()
    conteoCreditos.hide()
def salir():
    exit()
# Agregar Eventos

menuPrincipal.buttonCargar.clicked.connect(botonCargarArchivo)
menuPrincipal.buttonSalir.clicked.connect(salir)
menuPrincipal.buttonCursos.clicked.connect(buttonGesCursos)
menuPrincipal.buttonCreditos.clicked.connect(buttonAbrirConteo)

cargarArchivo.buttonRegresar.clicked.connect(regresarPrincipal)
cargarArchivo.buttonSelect.clicked.connect(buscarArchivo)
cargarArchivo.buttonCargar.clicked.connect(cargarFile)

gestionCursos.buttonRegresar.clicked.connect(buttonRegresar2)
gestionCursos.buttonLista.clicked.connect(buttonLista)
gestionCursos.buttonBuscar.clicked.connect(buttonBuscar)
gestionCursos.buttonAgregar.clicked.connect(buttonAbrirAgregar)
gestionCursos.buttonEditar.clicked.connect(buttonAbrirEditar)
gestionCursos.buttonEliminar.clicked.connect(buttonAbrirEliminar)

conteoCreditos.buttonRegresar.clicked.connect(buttonRegresar3)
conteoCreditos.buttonContar1.clicked.connect(buttonContar1)
conteoCreditos.buttonContar2.clicked.connect(buttonContar2)

listaCursos.buttonRegresar.clicked.connect(buttonRegresarLista)

buscarCurso.buttonRegresar.clicked.connect(buttonRegresarLista2)
buscarCurso.buttonBuscar.clicked.connect(buscar)

agregarCurso.buttonRegresar.clicked.connect(buttonRegresarLista3)
agregarCurso.buttonAgregar.clicked.connect(buttonAgregar)

editarCurso.buttonRegresar.clicked.connect(buttonRegresarLista4)
editarCurso.buttonEditar.clicked.connect(buttonEditar)
editarCurso.buttonBuscar.clicked.connect(buttonBuscar2)

eliminarCurso.buttonRegresar.clicked.connect(buttonRegresarLista5)
eliminarCurso.buttonEliminar.clicked.connect(buttonEliminar)

# Iniciar aplicacion
menuPrincipal.show()
app.exec()