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
        Roles.resize(940, 652)
        Roles.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.228856 rgba(223, 0, 255, 255), stop:0.761194 rgba(0, 186, 224, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Roles)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tenca = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tenca.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.tenca.setObjectName("tenca")
        self.gridLayout.addWidget(self.tenca, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.228856 rgba(223, 0, 255, 255), stop:0.761194 rgba(0, 186, 224, 255));\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.ConsultaVisites = QtWidgets.QWidget()
        self.ConsultaVisites.setObjectName("ConsultaVisites")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ConsultaVisites)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(27, 37, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
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
        self.tableWidget = QtWidgets.QTableWidget(parent=self.ConsultaVisites)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 2, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.ConsultaVisites)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 2, 0, 1, 2)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.ConsultaVisites)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 5, 1, 1, 1)
        self.Informe = QtWidgets.QTextEdit(parent=self.ConsultaVisites)
        self.Informe.setObjectName("Informe")
        self.gridLayout_2.addWidget(self.Informe, 5, 2, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 0, 1, 1)
        self.nom = QtWidgets.QLabel(parent=self.ConsultaVisites)
        self.nom.setText("")
        self.nom.setObjectName("nom")
        self.gridLayout_2.addWidget(self.nom, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.ConsultaVisites)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 2, 1, 1)
        self.cancelar = QtWidgets.QPushButton(parent=self.ConsultaVisites)
        self.cancelar.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.cancelar.setObjectName("cancelar")
        self.gridLayout_2.addWidget(self.cancelar, 7, 0, 1, 1)
        self.guardar = QtWidgets.QPushButton(parent=self.ConsultaVisites)
        self.guardar.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.guardar.setObjectName("guardar")
        self.gridLayout_2.addWidget(self.guardar, 7, 2, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.ConsultaVisites)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.ConsultaVisites)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 2)
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
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.HistorialDeVisites)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_2, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.HistorialDeVisites)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.HistorialDeVisites, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)
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
        self.tenca.setText(_translate("Roles", "Tancar Sessió"))
        self.usuari.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.label_2.setText(_translate("Roles", "Informe"))
        self.cancelar.setText(_translate("Roles", "Cancelar"))
        self.guardar.setText(_translate("Roles", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConsultaVisites), _translate("Roles", "Consulta Visites"))
        self.usuari_2.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HistorialDeVisites), _translate("Roles", "Historial de visites"))
        self.actionmeni.setText(_translate("Roles", "meni"))
        self.actiona.setText(_translate("Roles", "a"))
        self.actiona_2.setText(_translate("Roles", "a"))
