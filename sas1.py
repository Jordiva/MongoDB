from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Ejemplo de Popup")

        self.button = QPushButton("Agregar informe")
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.show_popup)

    def show_popup(self):
        popup = Popup()
        if popup.exec_() == QDialog.Accepted:
            informe = popup.informe.toPlainText()
            self.label.setText(informe)
            

class Popup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar informe")
        self.informe = QTextEdit()

        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(self.informe)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    app.exec_()
