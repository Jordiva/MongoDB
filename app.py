
from ctypes import cast
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from PyQt5 import QtWidgets, uic
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
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.jvalldaur
Usuaris = db["USUARIS"]
Metges = db["METGES"]   
Pacients = db["PACIENTS"]


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


def action_crear_contraseña():
    # agafar el nom del usuari que esta separat per espais

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


def action_Metge():
    print("Metge")


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


def gui_Pacients():
    Rols.hide()
    Contra_jaTe.hide()
    P_Pacient.show()


"""
def borra_txt_login():
    Login.errorusuari.setText("")
"""


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

# Buttons-menu Metge


Login.show()
app.exec()
