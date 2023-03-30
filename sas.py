from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class TableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Age', 'Delete'])

        data = [['John', '25'], ['Jane', '30'], ['Bob', '40']]

        for i, row in enumerate(data):
            self.tableWidget.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableWidget.setItem(i, j, newItem)

            deleteButton = QPushButton('Delete')
            deleteButton.clicked.connect(self.deleteRow)
            self.tableWidget.setCellWidget(i, 2, deleteButton)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def deleteRow(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            self.tableWidget.removeRow(index.row())

if __name__ == '__main__':
    app = QApplication([])
    window = TableWidgetExample()
    window.show()
    app.exec_()
