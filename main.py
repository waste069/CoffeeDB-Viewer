import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle("Add/Edit Coffee")
        self.coffee_id = coffee_id
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()

        # Validators for numeric input
        self.priceLineEdit.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.volumeLineEdit.setValidator(QIntValidator(0, 10000))

        if coffee_id is not None:
            self.load_coffee_data(coffee_id)

        self.saveButton.clicked.connect(self.save_coffee)

    def load_coffee_data(self, coffee_id):
        self.cursor.execute("SELECT * FROM coffee WHERE id = ?", (coffee_id,))
        coffee = self.cursor.fetchone()
        if coffee:
            self.sortNameLineEdit.setText(coffee[1])
            self.roastDegreeLineEdit.setText(coffee[2])
            self.groundBeansLineEdit.setText(coffee[3])
            self.tasteDescriptionTextEdit.setText(coffee[4])
            self.priceLineEdit.setText(str(coffee[5]))
            self.volumeLineEdit.setText(str(coffee[6]))

    def save_coffee(self):
        sort_name = self.sortNameLineEdit.text()
        roast_degree = self.roastDegreeLineEdit.text()
        ground_beans = self.groundBeansLineEdit.text()
        taste_description = self.tasteDescriptionTextEdit.toPlainText()
        price = self.priceLineEdit.text()
        package_volume = self.volumeLineEdit.text()

        if not all([sort_name, roast_degree, ground_beans, taste_description, price, package_volume]):
            print("Заполните все поля!")
            return

        try:
            price = float(price)
            package_volume = int(package_volume)
        except ValueError:
            print("Неверный формат числовых данных!")
            return

        if self.coffee_id is None:
            self.cursor.execute("""
                INSERT INTO coffee (sort_name, roast_degree, ground_or_beans, taste_description, price, package_volume)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (sort_name, roast_degree, ground_beans, taste_description, price, package_volume))
        else:
            self.cursor.execute("""
                UPDATE coffee
                SET sort_name = ?, roast_degree = ?, ground_or_beans = ?, taste_description = ?, price = ?, package_volume = ?
                WHERE id = ?
            """, (sort_name, roast_degree, ground_beans, taste_description, price, package_volume, self.coffee_id))

        self.conn.commit()
        self.close()


class CoffeeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем UI
        self.load_data()

        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()

        self.tableWidget.setRowCount(0)  # Очищаем таблицу
        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

        conn.close()

    def add_coffee(self):
        add_form = AddEditCoffeeForm(self)
        add_form.exec()
        self.load_data()

    def edit_coffee(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            coffee_id = int(self.tableWidget.item(selected_row, 0).text())
            edit_form = AddEditCoffeeForm(self, coffee_id)
            edit_form.exec()
            self.load_data()
        else:
            print("Выберите строку для редактирования.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = CoffeeViewer()
    viewer.show()
    sys.exit(app.exec())