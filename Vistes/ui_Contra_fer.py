# Form implementation generated from reading ui file 'c:\Users\jordi\Desktop\MongoBD\MongoDB\Vistes\Contra_fer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(522, 408)
        Login.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.637, y1:0.392364, x2:0.01, y2:0.994, stop:0 rgba(26, 255, 147, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 320, 181, 41))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton.setObjectName("pushButton")
        self.contra1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.contra1.setGeometry(QtCore.QRect(280, 90, 171, 31))
        self.contra1.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(176, 176, 176);")
        self.contra1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra1.setObjectName("contra1")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label.setObjectName("label")
        self.errorcontra = QtWidgets.QLabel(parent=self.centralwidget)
        self.errorcontra.setGeometry(QtCore.QRect(280, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.errorcontra.setFont(font)
        self.errorcontra.setObjectName("errorcontra")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 171, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.contra2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.contra2.setGeometry(QtCore.QRect(282, 170, 171, 31))
        self.contra2.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(176, 176, 176);")
        self.contra2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra2.setObjectName("contra2")
        self.usuari = QtWidgets.QLabel(parent=self.centralwidget)
        self.usuari.setGeometry(QtCore.QRect(20, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari.setFont(font)
        self.usuari.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.usuari.setObjectName("usuari")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 320, 171, 41))
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.usuari_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.usuari_2.setGeometry(QtCore.QRect(260, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari_2.setFont(font)
        self.usuari_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.usuari_2.setObjectName("usuari_2")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.pushButton.setText(_translate("Login", "Crear"))
        self.label.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contrasenya:</span></p></body></html>"))
        self.errorcontra.setText(_translate("Login", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Torna a escriure la</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Contrasenya:</span></p></body></html>"))
        self.usuari.setText(_translate("Login", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Login", "Back"))
        self.usuari_2.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Crea una contrasenya </span></p></body></html>"))
