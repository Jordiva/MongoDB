# Form implementation generated from reading ui file 'c:\Users\jordi\Desktop\MongoBD\MongoDB\Vistes\Roles.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Roles(object):
    def setupUi(self, Roles):
        Roles.setObjectName("Roles")
        Roles.resize(522, 408)
        Roles.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.228856 rgba(223, 0, 255, 255), stop:0.761194 rgba(0, 186, 224, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Roles)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
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
        self.gridLayout.addWidget(self.usuari, 0, 0, 1, 1)
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
        self.gridLayout.addWidget(self.usuari_3, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        Roles.setCentralWidget(self.centralwidget)

        self.retranslateUi(Roles)
        QtCore.QMetaObject.connectSlotsByName(Roles)

    def retranslateUi(self, Roles):
        _translate = QtCore.QCoreApplication.translate
        Roles.setWindowTitle(_translate("Roles", "Roles"))
        self.comboBox.setItemText(0, _translate("Roles", "Metge"))
        self.comboBox.setItemText(1, _translate("Roles", "Pacient"))
        self.pushButton.setText(_translate("Roles", "Entrar"))
        self.usuari.setText(_translate("Roles", "<html><head/><body><p><br/></p></body></html>"))
        self.usuari_3.setText(_translate("Roles", "<html><head/><body><p><span style=\" font-size:18pt;\">Escull Rol</span></p></body></html>"))