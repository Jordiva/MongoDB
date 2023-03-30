
from ctypes import cast
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton
import hashlib


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



#Verificar login
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

#comprovar si el usuari te contrasenya o no
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

#escollir el rol que te l'usuari
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


#Pantalla pacients demanar cita
def action_Pacient():

    dia= P_Pacient.comboBox.currentText()
    metge = P_Pacient.llista_metges.currentText()
    hora = P_Pacient.comboBox_2.currentText()
    
    #dades = llista_hores_metge()
    id_Metge = 0
    
    nomCompletMetge = None;
    #xagueda
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
    p2 = str( usuari.get("Cognoms"))
    nomComplertUsuari = p1 + " " + p2 
    if nomComplertUsuari == nomCompletMetge:
        P_Pacient.error.setText("No pots agafar cita amb tu mateix")
        P_Pacient.error.setStyleSheet("color: rgb(255, 0, 0);")
    else:
        #modificar 
        
        dia = dia.split("-")
        dia = dia[2] + "/" + dia[1] + "/" + dia[0]
        if hora != "":
            hora = hora + ":00"
            diacomplert = datetime.combine(datetime.strptime(dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
            misatge =  demanar_visita(id_Metge,id_usuari,usuari,diacomplert)
            P_Pacient.error.setText(misatge)
            P_Pacient.error.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            P_Pacient.error.setText("No has escollit hora")
            P_Pacient.error.setStyleSheet("color: rgb(255, 0, 0);")

#fer la cita retorna un missatge
def demanar_visita(id_metge,id_pacient, pacient,diahora):
    metge = Metges.find_one({"_id": id_metge})
    metge_usuaris = Usuaris.find_one({"_id": id_pacient})
    metgeNom = P_Pacient.llista_metges.currentText()
    missatge = "Error al demanar la cita"    
    if metge != None:
        for cita in metge['agenda']:
            if cita['moment_visita'] == diahora:
                cita['id_pacient'] = pacient['_id']
                Metges.update_one({'_id': id_metge}, {'$set': {'agenda': metge['agenda']}})
                missatge = "La teva visita amb el/la " + metgeNom + " ha estat demanada correctament Pel dia " + str(diahora)
                #borrar el seleccionado del combobox
                P_Pacient.comboBox_2.removeItem(P_Pacient.comboBox_2.currentIndex())
                global Dades 
                Dades= llista_hores_metge()
                P_Pacient.tableWidget.clearContents()
    return missatge

#tornar a la pantalla de login o tirar enrere
def action_back():
    Login.Usuari_name.setText("")
    Login.errorusuari.setText("")
    Contra_jaTe.contra1.setText("")
    Contra_jaTe.errorcontra.setText("")

    Contra_jaTe.hide()
    Contra_fer.hide()
    restablir_contra.hide()
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

#carrga la llista de metges
def gui_Pacients():
    Rols.hide()
    Contra_jaTe.hide()
    P_Pacient.show()
    #dades = llista_hores_metge()
    dades = Dades
    for dada in range(len(dades)):
        nom = dades[dada]
        P_Pacient.llista_metges.addItem(nom['nom'])

#mira si el metge cambia en el combobox
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
                    P_Pacient.comboBox.addItem(hora[i]['moment_visita'].strftime("%Y-%m-%d"))
                    tothors.append(hora[i]['moment_visita'].strftime("%d/%m/%Y"))

#mira el dia i al cambia depen de si es mou el combo box
def comboBoxChanged2():
    #dades = llista_hores_metge()
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
                        P_Pacient.comboBox_2.addItem(hora[i]['moment_visita'].strftime("%H:%M")) 

#no se si lutilitzo
def llista_metges():
    metges_ids = []
    metges_noms = []
    metges_cognoms= []
    nomComplert = []    
    for metges in Metges.find():
        metges_ids.append(metges['_id'])
        
    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_noms.append(metge['Nom'])
    
    for metge in Usuaris.find({'_id': {'$in': metges_ids}}):
        metges_cognoms.append(metge['Cognoms'])
        
    for i in range(len(metges_noms)):
        nomComplert.append(metges_noms[i]+" "+metges_cognoms[i])
        
        
    return nomComplert;

#si lo utilitzo retorna la llista de metges amb les hores
def llista_hores_metge():
    metges_ids = []
    metges_noms = []
    metges_cognoms= []
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
        horametge={'id': metges_ids[i], 'nom': nomComplert[i] , 'hores': Metges.find_one({"_id": metges_ids[i]}).get('agenda')}
        hores.append(horametge)  
    return hores
    
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
    P_Pacient.tableWidget.setHorizontalHeaderLabels(['Metge', 'Dia', 'Hora', 'Editar', 'Eliminar'])
    x = 0
    nom = P_Pacient.usuari.text()
    nom = nom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})
    id = usuari.get('_id')
    #buscar en la base de dades les visites del pacient i posar-les en la taula de la pestanya visites
    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        for i in range(len(hora)):
            if hora[i]['id_pacient'] == id:
                x = x +1 
    P_Pacient.tableWidget.setRowCount(x)
    y = 0
    for dada in range(len(Dades)):
        tot = Dades[dada]
        hora = tot['hores']
        for i in range(len(hora)):
            if hora[i]['id_pacient'] == id:
                P_Pacient.tableWidget.setItem( y ,0 ,QTableWidgetItem(tot['nom']))
                P_Pacient.tableWidget.setItem( y ,1 ,QTableWidgetItem(hora[i]['moment_visita'].strftime("%d/%m/%Y")))
                P_Pacient.tableWidget.setItem( y, 2 ,QTableWidgetItem(hora[i]['moment_visita'].strftime("%H:%M")))
                y = y + 1 
                
    for row in range(P_Pacient.tableWidget.rowCount()):
        button = QPushButton('Eliminar')
        buttoneditar = QPushButton('Editar')
        pos = P_Pacient.tableWidget.indexAt(button.pos())
        button.clicked.connect(lambda checked, row=row: eliminar_cita(row,pos))
        buttoneditar.clicked.connect(lambda checked, row=row: editar_cita(row,pos))
        P_Pacient.tableWidget.setCellWidget(row, P_Pacient.tableWidget.columnCount()-1, button)
        P_Pacient.tableWidget.setCellWidget(row, P_Pacient.tableWidget.columnCount()-2, buttoneditar)

    P_Pacient.llista_metges.clear()
    dades = Dades
    for dada in range(len(dades)):
        nom = dades[dada]
        P_Pacient.llista_metges.addItem(nom['nom'])


def editar_cita(row,pos):
    

def eliminar_cita(row,pos):
    print(row)
    
    nom = P_Pacient.usuari.text()
    nom = nom.split(" ")
    usuari = Usuaris.find_one({"login": nom[1]})
    
    medico = P_Pacient.tableWidget.item(row, 0).text()
    dia = P_Pacient.tableWidget.item(row, 1).text()
    hora = P_Pacient.tableWidget.item(row, 2).text()
    
    print(medico)
    print(dia)
    print(hora)
    
    #contar los espacios en blanco
    spais = medico.count(" ")
    print(spais)
    if pos.isValid():
        if (spais == 3):
            medico = medico.split(" ")
            print(medico)
            medi = medico[2]+" "+medico[3]
            medicos = Usuaris.find_one({"Cognoms": medi})
            print(medicos)
            idmetge = medicos.get('_id')
            
            if hora != "":
                dicionario = {"_id":0}
                hora = hora + ":00"
                diacomplert = datetime.combine(datetime.strptime(dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
                demanar_visita(idmetge,"0",dicionario,diacomplert)
                P_Pacient.tableWidget.removeRow(pos.row())
                P_Pacient.error_2.setText("Visita eliminada")
                tabChanged()
        else:
            medico = medico.split(" ")
            print(medico[0])
            medi = medico[1] + " " + medico[2]
            medicos = Usuaris.find_one({"Cognoms": medi})
            idmetge = medicos.get('_id')
            
            if hora != "":
                dicionario = {"_id":0}
                hora = hora + ":00"
                diacomplert = datetime.combine(datetime.strptime(dia, '%d/%m/%Y').date(), datetime.strptime(hora, '%H:%M:%S').time())
                demanar_visita(idmetge,"0",dicionario,diacomplert)
                P_Pacient.tableWidget.removeRow(pos.row())
                P_Pacient.error_2.setText("Visita eliminada")
                tabChanged()
        

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


# Buttons-menu Pacient

P_Pacient.pushButton.clicked.connect(action_Pacient)

P_Pacient.tabWidget.currentChanged.connect(tabChanged)


Dades = llista_hores_metge()

Login.show()
app.exec()
