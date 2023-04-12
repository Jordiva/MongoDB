
from ctypes import cast
import os
import time
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QComboBox, QAbstractItemView, QDialog, QLabel, QTextEdit, QPushButton, QVBoxLayout
import hashlib
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


app = QtWidgets.QApplication([])

# Login : Vistes.ui_Logni.Ui_Login = cast( Vistes.ui_Logni.Ui_Login, uic.loadUi("Vistes/Logni.ui"))
Login = uic.loadUi("Vistes/Logni.ui")
Contra_fer = uic.loadUi("Vistes/Contra_fer.ui")
Contra_jaTe = uic.loadUi("Vistes/Contra_jaTe.ui")
Rols = uic.loadUi("Vistes/Roles.ui")
restablir_contra = uic.loadUi("Vistes/restablir_contra.ui")
P_Metge = uic.loadUi("Vistes/Metge.ui")
P_Pacient = uic.loadUi("Vistes/Pacient.ui")

# usuari que te tot scastillo

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.jvalldaur
Usuaris = db["USUARIS"]
Metges = db["METGES"]
Pacients = db["PACIENTS"]
global Dades
global pacients


# Verificar login
def action_Login():

    Login.errorusuari.setText("")
    nom = Login.Usuari_name.text()

    usuari = Usuaris.find_one({"login": nom})

    if usuari == None:
        Login.errorusuari.setText("Usuari no trobat "+nom)
        Login.errorusuari.setStyleSheet("color: rgb(255, 0, 0);")
    else:
        Login.errorusuari.setText("Usuari trobat "+nom)
        Login.errorusuari.setStyleSheet("color: rgb(0, 255, 0);")
        contra = usuari.get("Contraseña")
        if contra == None:
            Contra_fer.usuari.setText("Usuari: "+nom)
            gui_enter()
        else:
            Contra_jaTe.usuari.setText("Usuari: "+nom)
            restablir_contra.usuari.setText("Usuari: "+nom)
            gui_Contra_jaTe()

# comprovar si el usuari te contrasenya o no


def comprova_contra():

    totnom = Contra_jaTe.usuari.text()
    nom = totnom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})

    contra = usuari.get("Contraseña")
    contraposada = Contra_jaTe.contra1.text()
    encriptContra = hashlib.sha256(contraposada.encode('utf-8'))
    if contra == "":
        Contra_jaTe.errorcontra.setText("Contrasenya buida")
        Contra_jaTe.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")

    elif contra == encriptContra.hexdigest():
        Contra_jaTe.errorcontra.setText("Contrasenya correcta")
        Contra_jaTe.errorcontra.setStyleSheet("color: rgb(0, 255, 0);")
        Contra_jaTe.contra1.setText("")
        Contra_jaTe.errorcontra.setText("")
        Contra_jaTe.usuari.setText("")

        id = usuari.get("_id")

        pacient = Pacients.find_one({"_id": id})
        metge = Metges.find_one({"_id": id})

        # mirar si es pacient o metge si es els dos portal a un altre lloc
        if pacient != None and metge != None:
            Rols.usuari.setText("Usuari: "+nom[1])
            gui_Rols()
        elif pacient != None:
            P_Pacient.usuari_2.setText("Pacient: "+nom[1])
            P_Pacient.usuari.setText("Pacient: "+nom[1])

            gui_Pacients()
        elif metge != None:
            P_Metge.usuari.setText("Metge: "+nom[1])
            P_Metge.usuari_2.setText("Metge: "+nom[1])

            gui_Metges()

    else:
        Contra_jaTe.errorcontra.setText("Contrasenya incorrecta")
        Contra_jaTe.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
        Contra_jaTe.contra1.setText("")

# restablir la contrasenya del usuari


def action_restablir_contar():

    totnom = restablir_contra.usuari.text()
    nom = totnom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})

    contra_Actual = usuari.get("Contraseña")

    vella = restablir_contra.contra.text()

    encriptContraVella = hashlib.sha256(vella.encode('utf-8')).hexdigest()

    nova = restablir_contra.contra1.text()
    nova_copia = restablir_contra.contra2.text()

    encriptContraNova = hashlib.sha256(nova.encode('utf-8')).hexdigest()

    # comprovar que los campos no sean vacios campos (vella nova nova_copia)
    if vella == "":
        restablir_contra.errorcontra.setText("Contrasenya buida")
        restablir_contra.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
    elif nova == "":
        restablir_contra.errorcontra.setText("Contrasenya buida")
        restablir_contra.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
    elif nova_copia == "":
        restablir_contra.errorcontra.setText("Contrasenya buida")
        restablir_contra.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
    else:
        if nova == nova_copia:
            if encriptContraVella == contra_Actual:
                if encriptContraNova != encriptContraVella:
                    Usuaris.update_one({"login": nom[1]}, {
                                       "$set": {"Contraseña": encriptContraNova}})
                    restablir_contra.errorcontra.setText(
                        "Contrasenya canviada")
                    restablir_contra.errorcontra.setStyleSheet(
                        "color: rgb(0, 255, 0);")
                    restablir_contra.contra.setText("")
                    restablir_contra.contra1.setText("")
                    restablir_contra.contra2.setText("")
                    restablir_contra.usuari.setText("")

                else:
                    restablir_contra.errorcontra.setText(
                        "La contrasenya nova no pot ser igual a la que tenies")
                    restablir_contra.errorcontra.setStyleSheet(
                        "color: rgb(255, 0, 0);")
            else:
                restablir_contra.errorcontra.setText(
                    "La contrasenya vella no es igual a la que tenies")
                restablir_contra.errorcontra.setStyleSheet(
                    "color: rgb(255, 0, 0);")

        else:
            restablir_contra.errorcontra.setText(
                "Contrasenyes no coincideixen")
            restablir_contra.errorcontra.setStyleSheet(
                "color: rgb(255, 0, 0);")

# Crear una contrasenya per un usuari


def action_crear_contraseña():
    totnom = Contra_fer.usuari.text()
    nom = totnom.split(" ")

    contra1 = Contra_fer.contra1.text()
    contra2 = Contra_fer.contra2.text()
    if contra1 == "":
        Contra_fer.errorcontra.setText("Contrasenya buida")
        Contra_fer.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
    elif contra2 == "":
        Contra_fer.errorcontra.setText("Contrasenya buida")
        Contra_fer.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
    else:
        if contra1 == contra2:
            Contra_fer.errorcontra.setText("Contrasenyes correctes")
            Contra_fer.errorcontra.setStyleSheet("color: rgb(0, 255, 0);")
            filtre = {'login': nom[1]}
            encript = hashlib.sha256(contra1.encode('utf-8'))
            newvalues = {"$set": {'Contraseña': encript.hexdigest()}}
            Usuaris.update_one(filtre, newvalues)
            Contra_fer.contra1.setText("")
            Contra_fer.contra2.setText("")
            Contra_fer.errorcontra.setText("")
            Contra_fer.usuari.setText("")
            action_back()
        else:
            Contra_fer.errorcontra.setText("Contrasenyes incorrectes")
            Contra_fer.errorcontra.setStyleSheet("color: rgb(255, 0, 0);")
            Contra_fer.contra1.setText("")
            Contra_fer.contra2.setText("")

# escollir el rol que te l'usuari


def action_rols_M_P():
    totnom = Rols.usuari.text()
    nom = totnom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})
    id = usuari.get("_id")

    rolAgafat = Rols.comboBox.currentText()

    if rolAgafat == "Metge":
        P_Metge.usuari.setText("Metge: "+nom[1])
        P_Metge.usuari_2.setText("Metge: "+nom[1])
        gui_Metges()
    if rolAgafat == "Pacient":
        P_Pacient.usuari.setText("Pacient: "+nom[1])
        P_Pacient.usuari_2.setText("Pacient: "+nom[1])
        gui_Pacients()


# Pantalla pacients demanar cita
def action_Pacient():

    dia = P_Pacient.comboBox.currentText()
    metge = P_Pacient.llista_metges.currentText()
    hora = P_Pacient.comboBox_2.currentText()

    # dades = llista_hores_metge()
    id_Metge = 0

    nomCompletMetge = None
    # xagueda
    dades = Dades

    for dada in range(len(dades)):
        tot = dades[dada]
        if metge == tot['nom']:
            id_Metge = tot['id']
            nomCompletMetge = tot['nom']
    usu = P_Pacient.usuari.text()
    usu = usu.split(" ")
    usuari = Usuaris.find_one({"login": usu[1]})
    id_usuari = usuari.get("_id")
    p1 = str(usuari.get("Nom"))
    p2 = str(usuari.get("Cognoms"))
    nomComplertUsuari = p1 + " " + p2
    if nomComplertUsuari == nomCompletMetge:
        P_Pacient.error.setText("No pots agafar cita amb tu mateix")
        P_Pacient.error.setStyleSheet("color: rgb(255, 0, 0);")
    else:
        # modificar

        dia = dia.split("-")
        dia = dia[2] + "/" + dia[1] + "/" + dia[0]
        if hora != "":
            hora = hora + ":00"
            diacomplert = datetime.combine(datetime.strptime(
                dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
            misatge = demanar_visita(id_Metge, id_usuari, usuari, diacomplert)
            P_Pacient.error.setText(misatge)
            P_Pacient.error.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            P_Pacient.error.setText("No has escollit hora")
            P_Pacient.error.setStyleSheet("color: rgb(255, 0, 0);")

# fer la cita retorna un missatge


def demanar_visita(id_metge, id_pacient, pacient, diahora):
    metge = Metges.find_one({"_id": id_metge})
    metge_usuaris = Usuaris.find_one({"_id": id_pacient})
    metgeNom = P_Pacient.llista_metges.currentText()
    missatge = "Error al demanar la cita"
    if metge != None:
        for cita in metge['agenda']:
            if cita['moment_visita'] == diahora:
                cita['id_pacient'] = pacient['_id']
                Metges.update_one({'_id': id_metge}, {
                                  '$set': {'agenda': metge['agenda']}})
                missatge = "La teva visita amb el/la " + metgeNom + \
                    " ha estat demanada correctament Pel dia " + str(diahora)
                # borrar el seleccionado del combobox
                P_Pacient.comboBox_2.removeItem(
                    P_Pacient.comboBox_2.currentIndex())
                global Dades
                Dades = llista_hores_metge()
                P_Pacient.tableWidget.clearContents()
    return missatge

# tornar a la pantalla de login o tirar enrere


def action_back():
    Login.Usuari_name.setText("")
    Login.errorusuari.setText("")
    Contra_jaTe.contra1.setText("")
    Contra_jaTe.errorcontra.setText("")

    Contra_jaTe.hide()
    Contra_fer.hide()
    restablir_contra.hide()
    P_Metge.hide()
    P_Pacient.hide()
    Login.show()


def gui_enter():
    Login.hide()
    Contra_fer.show()


def gui_Contra_jaTe():
    Login.hide()
    Contra_jaTe.show()


def gui_restablir_contra():
    Contra_jaTe.hide()
    restablir_contra.show()


def gui_Rols():
    Login.hide()
    Contra_jaTe.hide()
    Rols.show()


def gui_Metges():
    Contra_jaTe.hide()
    Rols.hide()
    P_Metge.show()

    metgeLogin = P_Metge.usuari.text()
    metgeLogin = metgeLogin.split(" ")

    metge = Usuaris.find_one({"login": metgeLogin[1]})
    id_metge = metge.get("_id")

    for dada in range(len(Dades)):
        metges = Dades[dada]
        if metges['id'] == id_metge:
            hora = metges['hores']
            for h in range(len(hora)):
                if hora[h]['id_pacient'] != 0:
                    if hora[h]['realitzada'] == 'n':
                        highlight_date(QDate(int(hora[h]['moment_visita'].year), int(
                            hora[h]['moment_visita'].month), int(hora[h]['moment_visita'].day)))


def highlight_date(date):
    # Definir el formato de texto para resaltar el día
    date_format = QTextCharFormat()
    date_format.setBackground(QBrush(QColor('red')))

    # Resaltar el día en el calendario
    P_Metge.calendarWidget.setDateTextFormat(date, date_format)

# carrga la llista de metges


def gui_Pacients():
    Rols.hide()
    Contra_jaTe.hide()
    P_Pacient.show()
    # dades = llista_hores_metge()
    dades = Dades
    for dada in range(len(dades)):
        nom = dades[dada]
        P_Pacient.llista_metges.addItem(nom['nom'])


# mira si el metge cambia en el combobox
def comboBoxChanged():

    P_Pacient.error.setText("")

    metge = P_Pacient.llista_metges.currentText()

    tothors = []
    P_Pacient.comboBox.clear()
    dades = Dades

    for dada in range(len(dades)):
        tot = dades[dada]
        hora = tot['hores']
        if tot['nom'] == metge:
            for i in range(len(hora)):
                if hora[i]['moment_visita'].strftime("%d/%m/%Y") not in tothors:
                    P_Pacient.comboBox.addItem(
                        hora[i]['moment_visita'].strftime("%Y-%m-%d"))
                    tothors.append(
                        hora[i]['moment_visita'].strftime("%d/%m/%Y"))

# mira el dia i al cambia depen de si es mou el combo box


def comboBoxChanged2():
    # dades = llista_hores_metge()
    P_Pacient.error.setText("")

    dia = P_Pacient.comboBox.currentText()
    metge = P_Pacient.llista_metges.currentText()
    P_Pacient.comboBox_2.clear()

    dades = Dades

    for dada in range(len(dades)):
        tot = dades[dada]
        hora = tot['hores']
        if tot['nom'] == metge:
            for i in range(len(hora)):
                if hora[i]['moment_visita'].strftime("%Y-%m-%d") == dia:
                    if hora[i]['id_pacient'] == 0:
                        P_Pacient.comboBox_2.addItem(
                            hora[i]['moment_visita'].strftime("%H:%M"))

# no se si lutilitzo


def llista_metges():
    metges_ids = []
    metges_noms = []
    metges_cognoms = []
    nomComplert = []
    for metges in Metges.find():
        metges_ids.append(metges['_id'])

    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_noms.append(metge['Nom'])

    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_cognoms.append(metge['Cognoms'])

    for i in range(len(metges_noms)):
        nomComplert.append(metges_noms[i]+" "+metges_cognoms[i])

    return nomComplert

# si lo utilitzo retorna la llista de metges amb les hores


def llista_hores_metge():
    metges_ids = []
    metges_noms = []
    metges_cognoms = []
    nomComplert = []
    hores = []
    horametge = {}

    for metges in Metges.find():
        metges_ids.append(metges['_id'])

    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_noms.append(metge['Nom'])

    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_cognoms.append(metge['Cognoms'])

    for i in range(len(metges_noms)):
        nomComplert.append(metges_noms[i]+" "+metges_cognoms[i])

    for i in range(len(metges_ids)):
        horametge = {'id': metges_ids[i], 'nom': nomComplert[i], 'hores': Metges.find_one(
            {"_id": metges_ids[i]}).get('agenda')}
        hores.append(horametge)
    return hores


def pacients_llista():
    pacients_ids = []
    pacients_noms = []
    tot_id_nom = {}
    pacientsfin = []

    for pacients in Pacients.find():
        pacients_ids.append(pacients['_id'])

    for pacient in Usuaris.find({'_id': {'$in': pacients_ids}}):
        pacients_noms.append(pacient['Nom'] + " " + pacient['Cognoms'])

    for i in range(len(pacients_ids)):
        tot_id_nom = {'id': pacients_ids[i], 'nom': pacients_noms[i]}
        pacientsfin.append(tot_id_nom)

    return pacientsfin


def changeComboMetge():

    nom = P_Metge.comboBox.currentText()
    print(nom)
    id_paciente = 0
    # print(pacients)
    for ias in pacients:
        if ias['nom'] == nom:
            id_paciente = ias['id']

    print(id_paciente)

    table = P_Metge.tableWidget_2
    table.setRowCount(0)
    table.setColumnCount(4)
    table.setHorizontalHeaderLabels(['Nombre', 'Fecha', 'Metge', 'Informe'])

    table.setColumnWidth(0, 150)  # Nombre
    table.setColumnWidth(1, 100)  # Fecha
    table.setColumnWidth(2, 150)  # Metge
    table.setColumnWidth(3, 400)  # Informe

    row = 0
    for i in range(len(Dades)):
        tot = Dades[i]
        hora = tot['hores']
        for j in range(len(hora)):
            if hora[j]['id_pacient'] == id_paciente:
                if hora[j]['realitzada'] == 's':
                    table.insertRow(row)
                    table.setItem(row, 0, QTableWidgetItem(nom))
                    table.setItem(row, 1, QTableWidgetItem(
                        hora[j]['moment_visita'].strftime("%Y-%m-%d")))
                    table.setItem(row, 3, QTableWidgetItem(hora[j]['informe']))
                    table.setItem(row, 2, QTableWidgetItem(tot['nom']))
                    row += 1

    for i in range(table.rowCount()):
        table.setRowHeight(i, 30)

    table.sortItems(1, Qt.AscendingOrder)


# no se si lutilitzo
def llista_metges_hores():
    list_metges = []
    dict_metges = {}
    for metge in Metges.find():
        metge_id = metge.get('_id')
        metge_nom = Usuaris.find_one({"_id": metge_id}).get('Nom')
        metge_cognoms = Usuaris.find_one({"_id": metge_id}).get('Cognoms')
        metge_nom_complet = metge_nom + " " + metge_cognoms
        dict_metges = {'id': metge_id, 'nom': metge_nom_complet}
        list_metges.append(dict_metges)
    return list_metges


def tabChanged():
    P_Pacient.tableWidget.setColumnCount(5)
    P_Pacient.tableWidget.setHorizontalHeaderLabels(
        ['Metge', 'Dia', 'Hora', 'Editar', 'Eliminar'])
    x = 0
    nom = P_Pacient.usuari.text()
    nom = nom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})
    id = usuari.get('_id')
    # buscar en la base de dades les visites del pacient i posar-les en la taula de la pestanya visites
    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        for i in range(len(hora)):
            if hora[i]['id_pacient'] == id:
                x = x + 1
    P_Pacient.tableWidget.setRowCount(x)
    y = 0
    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        for i in range(len(hora)):
            if hora[i]['id_pacient'] == id:
                P_Pacient.tableWidget.setItem(
                    y, 0, QTableWidgetItem(tot['nom']))
                P_Pacient.tableWidget.setItem(y, 1, QTableWidgetItem(
                    hora[i]['moment_visita'].strftime("%d/%m/%Y")))
                P_Pacient.tableWidget.setItem(y, 2, QTableWidgetItem(
                    hora[i]['moment_visita'].strftime("%H:%M")))
                y = y + 1

    for row in range(P_Pacient.tableWidget.rowCount()):
        button = QPushButton('Eliminar')
        buttoneditar = QPushButton('Editar')
        pos = P_Pacient.tableWidget.indexAt(button.pos())
        button.clicked.connect(
            lambda checked, row=row: eliminar_cita(row, pos))
        buttoneditar.clicked.connect(
            lambda checked, row=row: convert_to_combobox(P_Pacient.tableWidget, row))
        P_Pacient.tableWidget.setCellWidget(
            row, P_Pacient.tableWidget.columnCount()-1, button)
        P_Pacient.tableWidget.setCellWidget(
            row, P_Pacient.tableWidget.columnCount()-2, buttoneditar)

    P_Pacient.llista_metges.clear()
    dades = Dades
    for dada in range(len(dades)):
        nom = dades[dada]
        P_Pacient.llista_metges.addItem(nom['nom'])


def convert_to_combobox(table, row):
    # Obtener la celda correspondiente en la columna 1
    cell = table.item(row, 1)

    # Crear un cuadro combinado y agregar las opciones
    combo_box = QComboBox()
    combo_box1 = QComboBox()

    metge = table.item(row, 0).text()
    dia = table.item(row, 1).text()
    # hora = P_Pacient.tableWidget.item(row, 2).text()
    dia = dia.split("/")
    dia = dia[2] + "-" + dia[1] + "-" + dia[0]
    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        if tot['nom'] == metge:
            for i in range(len(hora)):
                if hora[i]['moment_visita'].strftime("%Y-%m-%d") == dia:
                    if hora[i]['id_pacient'] == 0:
                        combo_box1.addItem(
                            hora[i]['moment_visita'].strftime("%H:%M"))

    tothors = []

    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        if tot['nom'] == metge:
            for i in range(len(hora)):
                if hora[i]['moment_visita'].strftime("%d/%m/%Y") not in tothors:
                    combo_box.addItem(
                        hora[i]['moment_visita'].strftime("%Y-%m-%d"))
                    tothors.append(
                        hora[i]['moment_visita'].strftime("%d/%m/%Y"))

    # Seleccionar la opción correspondiente al texto de la celda
    index = combo_box.findText(cell.text())
    if index >= 0:
        combo_box.setCurrentIndex(index)

    # Reemplazar la celda con el cuadro combinado
    table.setCellWidget(row, 1, combo_box)
    table.setCellWidget(row, 2, combo_box1)

    # Agregar un botón "Aceptar" y desactivar el botón "Eliminar"
    button_accept = QPushButton('Aceptar')
    button_accept.clicked.connect(
        lambda checked, row=row: accept_changes(table, row, combo_box, combo_box1))
    table.setCellWidget(row, 3, button_accept)
    table.cellWidget(row, 4).setEnabled(False)


def accept_changes(table, row, combo_box, combo_box1):
    dataVella = table.item(row, 1).text()
    dataNova = combo_box.currentText()

    horaVella = table.item(row, 2).text()
    horaNova = combo_box1.currentText()

    metge = table.item(row, 0).text()

    horas = horaNova

    dataVella = dataVella.split("/")
    dataVella = dataVella[0] + "/" + dataVella[1] + "/" + dataVella[2]
    dataNova = dataNova.split("-")
    dataNova = dataNova[2] + "/" + dataNova[1] + "/" + dataNova[0]
    horaVella = horaVella + ":00"
    horaNova = horaNova + ":00"

    DiaVell = datetime.combine(datetime.strptime(
        dataVella, '%d/%m/%Y').date(), datetime.strptime(horaVella, '%H:%M:%S').time())
    DiaNou = datetime.combine(datetime.strptime(
        dataNova, '%d/%m/%Y').date(), datetime.strptime(horaNova, '%H:%M:%S').time())

    pacient = P_Pacient.usuari_2.text()

    pacient = pacient.split(" ")
    usuari = Usuaris.find_one({"login": pacient[1]})

    idusuari = usuari.get('_id')

    # Reemplazar el cuadro combinado con un objeto QTableWidgetItem
    dia = QTableWidgetItem(dataNova)
    hora = QTableWidgetItem(horas)
    table.setItem(row, 1, dia)
    table.setItem(row, 2, hora)
    messatge = ""
    spais = metge.count(" ")
    if (spais == 3):
        medico = metge.split(" ")
        medi = medico[2]+" "+medico[3]
        medicos = Usuaris.find_one({"Cognoms": medi})
        idmetge = medicos.get('_id')
        dicionario = {"_id": 0}
        messatge = Update_visiata(idmetge, dicionario, usuari, DiaVell, DiaNou)
    else:

        medico = metge.split(" ")
        medi = medico[1] + " " + medico[2]
        medicos = Usuaris.find_one({"Cognoms": medi})
        idmetge = medicos.get('_id')
        dicionario = {"_id": 0}
        messatge = Update_visiata(idmetge, dicionario, usuari, DiaVell, DiaNou)

    """
    button_accept = QPushButton('Editar')
    button_accept.clicked.connect(lambda checked, row=row: convert_to_combobox(table, row))
    table.setCellWidget(row, 3, button_accept)
    """

    table.cellWidget(row, 4).setEnabled(True)

    if isinstance(table.cellWidget(row, 2), QComboBox):
        combo_box.deleteLater()
        combo_box1.deleteLater()

    P_Pacient.error_2.setText(messatge)
    table.clearContents()
    # hacer una pausa de 1 segundo
    time.sleep(1)
    tabChanged()


def eliminar_cita(row, pos):

    nom = P_Pacient.usuari.text()
    nom = nom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})

    medico = P_Pacient.tableWidget.item(row, 0).text()
    dia = P_Pacient.tableWidget.item(row, 1).text()
    hora = P_Pacient.tableWidget.item(row, 2).text()

    # contar los espacios en blanco
    spais = medico.count(" ")
    if pos.isValid():
        if (spais == 3):
            medico = medico.split(" ")
            medi = medico[2]+" "+medico[3]
            medicos = Usuaris.find_one({"Cognoms": medi})
            idmetge = medicos.get('_id')

            if hora != "":
                dicionario = {"_id": 0}
                hora = hora + ":00"
                diacomplert = datetime.combine(datetime.strptime(
                    dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
                demanar_visita(idmetge, "0", dicionario, diacomplert)
                P_Pacient.tableWidget.removeRow(pos.row())
                P_Pacient.error_2.setText("Visita eliminada")
                tabChanged()
        else:
            medico = medico.split(" ")
            medi = medico[1] + " " + medico[2]
            medicos = Usuaris.find_one({"Cognoms": medi})
            idmetge = medicos.get('_id')

            if hora != "":
                dicionario = {"_id": 0}
                hora = hora + ":00"
                diacomplert = datetime.combine(datetime.strptime(
                    dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
                demanar_visita(idmetge, "0", dicionario, diacomplert)
                P_Pacient.tableWidget.removeRow(pos.row())
                P_Pacient.error_2.setText("Visita eliminada")
                tabChanged()


def tabChangedMetge():

    P_Metge.comboBox.clear()
    for i in pacients:
        P_Metge.comboBox.addItem(i['nom'])


def Update_visiata(id_metge, pacientantic, pacientnou, diahoraAntiga, diahoraNova):
    metge = Metges.find_one({"_id": id_metge})
    metgeNom = P_Pacient.llista_metges.currentText()
    missatge = "Error al demanar la cita"
    if metge != None:
        for cita in metge['agenda']:
            if cita['moment_visita'] == diahoraAntiga:
                cita['id_pacient'] = pacientantic['_id']
                Metges.update_one({'_id': id_metge}, {
                                  '$set': {'agenda': metge['agenda']}})
                # borrar el seleccionado del combobox
            if cita['moment_visita'] == diahoraNova:
                cita['id_pacient'] = pacientnou['_id']
                Metges.update_one({'_id': id_metge}, {
                                  '$set': {'agenda': metge['agenda']}})
                global Dades
                Dades = llista_hores_metge()
                missatge = "Cita modificada"

    return missatge


def action_calendar():
    date = P_Metge.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    tabla = P_Metge.tableWidget

    P_Metge.label.setText("")

    tabla.clearContents()
    fila = tabla.setRowCount(0)
    tabla.setColumnCount(3)
    tabla.setHorizontalHeaderLabels(["Nom Pacient", "Hora", "Día"])
    tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
    metgeLogin = P_Metge.usuari.text()
    metgeLogin = metgeLogin.split(" ")

    metge = Usuaris.find_one({"login": metgeLogin[1]})
    id_metge = metge.get("_id")

    def on_table_cell_clicked(row, col):
        nom = tabla.item(row, 0).text()
        dia = tabla.item(row, 2).text()
        hora = tabla.item(row, 1).text()

        P_Metge.nom.setText(nom)
        P_Metge.dateEdit.setDate(datetime.strptime(dia, '%Y-%m-%d').date())
        P_Metge.timeEdit.setTime(datetime.strptime(hora, '%H:%M:%S').time())
        P_Metge.Informe.setText("")

    row = tabla.cellClicked.connect(on_table_cell_clicked)

    for dada in range(len(Dades)):
        metges = Dades[dada]
        if metges['id'] == id_metge:
            hora = metges['hores']
            for h in range(len(hora)):
                if hora[h]['id_pacient'] != 0:
                    if hora[h]['realitzada'] == 'n':
                        if hora[h]['moment_visita'].strftime("%Y-%m-%d") == date:
                            fila = tabla.rowCount()
                            tabla.insertRow(fila)

                            # Agregar los datos a las celdas de la fila
                            id_paciente = hora[h]['id_pacient']
                            hora_visita = hora[h]['moment_visita'].strftime(
                                "%H:%M:%S")
                            dia_visita = hora[h]['moment_visita'].strftime(
                                "%Y-%m-%d")

                            p = Usuaris.find_one({"_id": id_paciente})
                            nom = p['Nom'] + " " + p['Cognoms']

                            tabla.setItem(fila, 0, QTableWidgetItem(str(nom)))
                            tabla.setItem(
                                fila, 1, QTableWidgetItem(str(hora_visita)))
                            tabla.setItem(
                                fila, 2, QTableWidgetItem(str(dia_visita)))


def borra_información():
    invalid_date = QDate.fromString("01-01-0001", "dd-MM-yyyy")
    invalid_time = QTime.fromString("00:00:00", "hh:mm:ss")
    P_Metge.nom.setText("")
    P_Metge.dateEdit.setDate(invalid_date)
    P_Metge.timeEdit.setTime(invalid_time)
    P_Metge.Informe.setText("")


def actualitzar_informe():
    metgeLogin = P_Metge.usuari.text()
    metgeLogin = metgeLogin.split(" ")

    metges = Usuaris.find_one({"login": metgeLogin[1]})
    id_metge = metges.get("_id")

    metge = Metges.find_one({"_id": id_metge})

    nom = P_Metge.nom.text()

    dia = P_Metge.dateEdit.text()
    hora = P_Metge.timeEdit.text()
    dia = dia.split("/")
    dia = dia[0]+"/"+dia[1]+"/"+dia[2]

    hora = hora + ":00"
    diacomplert = datetime.combine(datetime.strptime(
        dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
    if metge != None:
        for cita in metge['agenda']:
            if cita['moment_visita'] == diacomplert:
                if P_Metge.Informe.toPlainText() != "":
                    if nom != "":
                        cita['informe'] = P_Metge.Informe.toPlainText()
                        cita['realitzada'] = 's'
                        Metges.update_one({'_id': id_metge}, {
                                          '$set': {'agenda': metge['agenda']}})
                        global Dades
                        Dades = llista_hores_metge()
                        borra_información()
                        P_Metge.label.setText("Informe actualizado")
                        P_Metge.label.setStyleSheet("color: green")

                    else:
                        P_Metge.label.setText(
                            "No has seleccionado ninguna cita")
                        P_Metge.label.setStyleSheet("color: red")
                else:
                    P_Metge.label.setText("No has escrito ningún informe")
                    P_Metge.label.setStyleSheet("color: red")


    Login.show()
    P_Metge.close()
    P_Pacient.close()



# Buttonns Login
# Login.Usuari_name.textEdited.connect(borra_txt_login)
Login.pushButton.clicked.connect(action_Login)

# Buttons Contra_fer
Contra_fer.pushButton_2.clicked.connect(action_back)
Contra_fer.pushButton.clicked.connect(action_crear_contraseña)

# Buttons Contra_jaTe
Contra_jaTe.pushButton_5.clicked.connect(action_back)
Contra_jaTe.pushButton_3.clicked.connect(comprova_contra)
Contra_jaTe.pushButton_4.clicked.connect(gui_restablir_contra)

# Buttons contrasenya restablir
restablir_contra.pushButton.clicked.connect(action_restablir_contar)
restablir_contra.pushButton_2.clicked.connect(action_back)

# Buttons Rols-M-P
Rols.pushButton.clicked.connect(action_rols_M_P)
P_Pacient.llista_metges.currentIndexChanged.connect(comboBoxChanged)
P_Pacient.comboBox.currentIndexChanged.connect(comboBoxChanged2)

# Buttons-menu Metge

P_Metge.calendarWidget.clicked.connect(action_calendar)
P_Metge.cancelar.clicked.connect(borra_información)
P_Metge.guardar.clicked.connect(actualitzar_informe)

P_Metge.tabWidget.currentChanged.connect(tabChangedMetge)
P_Metge.comboBox.currentIndexChanged.connect(changeComboMetge)
# Buttons-menu Pacient

P_Pacient.pushButton.clicked.connect(action_Pacient)

P_Pacient.tabWidget.currentChanged.connect(tabChanged)


#tenca sessió

P_Metge.tenca.clicked.connect(action_back)
P_Pacient.tenca.clicked.connect(action_back)

Dades = llista_hores_metge()
pacients = pacients_llista()

Login.show()
app.exec()
