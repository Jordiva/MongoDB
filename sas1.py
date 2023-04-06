from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

# crear una instancia del QTableWidget
table = QTableWidget()

# seleccionar una fila
selected_items = table.selectedItems()
if len(selected_items) > 0:
    selected_item = selected_items[0]
    row_index = selected_item.row()
    print(f"Se ha seleccionado la fila {row_index}")
else:
    print("No se ha seleccionado ninguna fila")
