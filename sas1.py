from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QComboBox

app = QApplication([])

# Crear la tabla con 3 filas y 4 columnas
table = QTableWidget(3, 4)

# Agregar botones al final de cada fila
for row in range(table.rowCount()):
    button_convert = QPushButton('Convertir a ComboBox')
    button_convert.clicked.connect(lambda checked, row=row: convert_to_combobox(table, row))
    table.setCellWidget(row, 2, button_convert)

    button_delete = QPushButton('Eliminar')
    button_delete.clicked.connect(lambda checked, row=row: delete_row(table, row))
    table.setCellWidget(row, 3, button_delete)

# Función para convertir una celda en un cuadro combinado
def convert_to_combobox(table, row):
    # Obtener la celda correspondiente en la columna 1
    cell = table.item(row, 1)

    # Crear un cuadro combinado y agregar las opciones
    combo_box = QComboBox()
    combo_box.addItems(['Opción 1', 'Opción 2', 'Opción 3'])

    # Seleccionar la opción correspondiente al texto de la celda
    index = combo_box.findText(cell.text())
    if index >= 0:
        combo_box.setCurrentIndex(index)

    # Reemplazar la celda con el cuadro combinado
    table.setCellWidget(row, 1, combo_box)

    # Agregar un botón "Aceptar" y desactivar el botón "Eliminar"
    button_accept = QPushButton('Aceptar')
    button_accept.clicked.connect(lambda checked, row=row, combo_box=combo_box: accept_changes(table, row, combo_box))
    table.setCellWidget(row, 2, button_accept)
    table.cellWidget(row, 3).setEnabled(False)

# Función para aceptar los cambios y volver a un texto normal
def accept_changes(table, row, combo_box):
    # Obtener el índice seleccionado y el texto correspondiente
    index = combo_box.currentIndex()
    text = combo_box.currentText()

    # Reemplazar el cuadro combinado con un objeto QTableWidgetItem
    item = QTableWidgetItem(text)
    table.setItem(row, 1, item)

    # Restablecer el botón "Convertir" y habilitar el botón "Eliminar"
    button_convert = QPushButton('Convertir a ComboBox')
    button_convert.clicked.connect(lambda checked, row=row: convert_to_combobox(table, row))
    table.setCellWidget(row, 2, button_convert)
    table.cellWidget(row, 3).setEnabled(True)

    # Ocultar el cuadro combinado si existe
    if isinstance(table.cellWidget(row, 1), QComboBox):
        combo_box.deleteLater()
        

# Función para eliminar una fila
def delete_row(table, row):
    table.removeRow(row)

# Agregar algunos datos de ejemplo
table.setItem(0, 0, QTableWidgetItem('A1'))
table.setItem(0, 1, QTableWidgetItem('B1'))
table.setItem(1, 0, QTableWidgetItem('A2'))
table.setItem(1, 1, QTableWidgetItem('B2'))
table.setItem(2, 0, QTableWidgetItem('A3'))
table.setItem(2, 1, QTableWidgetItem('B3'))

# Mostrar la tabla
table.show()

# Ejecutar la aplicación
app.exec_()
