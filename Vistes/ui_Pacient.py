# Form implementation generated from reading ui file 'c:\Users\jordi\Desktop\MongoBD\MongoDB\Vistes\Pacient.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Roles(object):
    def setupUi(self, Roles):
        Roles.setObjectName("Roles")
        Roles.resize(678, 472)
        Roles.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.637, y1:0.392364, x2:0.01, y2:0.994, stop:0 rgba(26, 255, 147, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Roles)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.DemanarHora = QtWidgets.QWidget()
        self.DemanarHora.setObjectName("DemanarHora")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.DemanarHora)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.DemanarHora)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.DemanarHora)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.DemanarHora)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 201, 176);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 9, 2, 1, 1)
        self.usuari = QtWidgets.QLabel(parent=self.DemanarHora)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usuari.setFont(font)
        self.usuari.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: black;")
        self.usuari.setObjectName("usuari")
        self.gridLayout_2.addWidget(self.usuari, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 2, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.DemanarHora)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 1, 2, 1, 1)
        self.llista_metges = QtWidgets.QComboBox(parent=self.DemanarHora)
        self.llista_metges.setObjectName("llista_metges")
        self.gridLayout_2.addWidget(self.llista_metges, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 1, 1)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(parent=self.DemanarHora)
        self.calendarWidget_2.setStyleSheet("font:20px;")
        self.calendarWidget_2.setGridVisible(False)
        self.calendarWidget_2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_2.addWidget(self.calendarWidget_2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.DemanarHora, "")
        self.ConsultaVisites = QtWidgets.QWidget()
        self.ConsultaVisites.setObjectName("ConsultaVisites")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ConsultaVisites)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.usuari_2 = QtWidgets.QLabel(parent=self.ConsultaVisites)
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
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.ConsultaVisites)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.ConsultaVisites)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_3.addWidget(self.calendarWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.ConsultaVisites, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        Roles.setCentralWidget(self.centralwidget)

        self.retranslateUi(Roles)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Roles)

    def retranslateUi(self, Roles):
        _translate = QtCore.QCoreApplication.translate
        Roles.setWindowTitle(_translate("Roles", "Pacient"))
        self.label_2.setText(_translate("Roles", "Metges"))
        self.label_3.setText(_translate("Roles", "Hora a Demanar"))
        self.pushButton.setText(_translate("Roles", "Demanar"))
        self.usuari.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.timeEdit.setDisplayFormat(_translate("Roles", "HH:mm:ss"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DemanarHora), _translate("Roles", "Demanar Hora"))
        self.usuari_2.setText(_translate("Roles", "<html><head/><body><p>sa</p></body></html>"))
        self.pushButton_2.setText(_translate("Roles", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConsultaVisites), _translate("Roles", "Consulta Visites"))
