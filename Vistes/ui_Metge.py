# Form implementation generated from reading ui file 'c:\Users\jordi\Desktop\MongoBD\MongoDB\Vistes\Metge.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Roles(object):
    def setupUi(self, Roles):
        Roles.setObjectName("Roles")
        Roles.resize(651, 470)
        Roles.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.637, y1:0.392364, x2:0.01, y2:0.994, stop:0 rgba(26, 255, 147, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Roles)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.ConsultaVisites = QtWidgets.QWidget()
        self.ConsultaVisites.setObjectName("ConsultaVisites")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ConsultaVisites)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.usuari = QtWidgets.QLabel(parent=self.ConsultaVisites)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari.setFont(font)
        self.usuari.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: Black;")
        self.usuari.setObjectName("usuari")
        self.gridLayout_2.addWidget(self.usuari, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.ConsultaVisites)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        self.tabWidget.addTab(self.ConsultaVisites, "")
        self.HistorialDeVisites = QtWidgets.QWidget()
        self.HistorialDeVisites.setObjectName("HistorialDeVisites")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.HistorialDeVisites)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.usuari_2 = QtWidgets.QLabel(parent=self.HistorialDeVisites)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari_2.setFont(font)
        self.usuari_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: Black;")
        self.usuari_2.setObjectName("usuari_2")
        self.gridLayout_3.addWidget(self.usuari_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.HistorialDeVisites)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.tabWidget.addTab(self.HistorialDeVisites, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        Roles.setCentralWidget(self.centralwidget)
        self.actionmeni = QtGui.QAction(parent=Roles)
        self.actionmeni.setObjectName("actionmeni")
        self.actiona = QtGui.QAction(parent=Roles)
        self.actiona.setObjectName("actiona")
        self.actiona_2 = QtGui.QAction(parent=Roles)
        self.actiona_2.setObjectName("actiona_2")

        self.retranslateUi(Roles)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Roles)

    def retranslateUi(self, Roles):
        _translate = QtCore.QCoreApplication.translate
        Roles.setWindowTitle(_translate("Roles", "Metge"))
        self.usuari.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.pushButton.setText(_translate("Roles", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConsultaVisites), _translate("Roles", "Consulta Visites"))
        self.usuari_2.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.pushButton_2.setText(_translate("Roles", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HistorialDeVisites), _translate("Roles", "Historial de visites"))
        self.actionmeni.setText(_translate("Roles", "meni"))
        self.actiona.setText(_translate("Roles", "a"))
        self.actiona_2.setText(_translate("Roles", "a"))
