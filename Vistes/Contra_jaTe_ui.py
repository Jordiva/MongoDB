# Form implementation generated from reading ui file 'c:\Users\jordi\Desktop\MongoBD\MongoDB\Vistes\Contra_jaTe.ui'
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
        Login.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.228856 rgba(223, 0, 255, 255), stop:0.761194 rgba(0, 186, 224, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.usuari = QtWidgets.QLabel(parent=self.centralwidget)
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
        self.gridLayout.addWidget(self.usuari, 0, 1, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 2)
        self.usuari_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari_3.setFont(font)
        self.usuari_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.usuari_3.setObjectName("usuari_3")
        self.gridLayout.addWidget(self.usuari_3, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)
        self.contra1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.contra1.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(176, 176, 176);")
        self.contra1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra1.setObjectName("contra1")
        self.gridLayout.addWidget(self.contra1, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.errorcontra = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.errorcontra.setFont(font)
        self.errorcontra.setObjectName("errorcontra")
        self.gridLayout.addWidget(self.errorcontra, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 2, 2, 1)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.usuari.setText(_translate("Login", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("Login", "Cambiar contrasenya"))
        self.usuari_3.setText(_translate("Login", "<html><head/><body><p>Entra la contrasenya </p></body></html>"))
        self.pushButton_3.setText(_translate("Login", "Entrar"))
        self.pushButton_5.setText(_translate("Login", "Back"))
        self.label.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:20pt;\">Contrasenya:</span></p></body></html>"))
        self.errorcontra.setText(_translate("Login", "<html><head/><body><p><br/></p></body></html>"))