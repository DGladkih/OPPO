import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from datetime import datetime

class Product:
    def __init__(self, name, quantity, date):
        self.name = name
        self.quantity = quantity
        self.date = date

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.created_product = None  # Добавляем переменную для хранения созданного товара

    def init_ui(self):
        self.setWindowTitle('Создание товара')
        self.setGeometry(300, 300, 300, 200)

        self.name_label = QLabel('Название товара:', self)
        self.name_label.move(20, 20)
        self.name_input = QLineEdit(self)
        self.name_input.move(150, 20)

        self.quantity_label = QLabel('Количество:', self)
        self.quantity_label.move(20, 50)
        self.quantity_input = QLineEdit(self)
        self.quantity_input.move(150, 50)

        self.create_button = QPushButton('Создать товар', self)
        self.create_button.move(100, 100)
        self.create_button.clicked.connect(self.create_product)

        self.show()

    def create_product(self):
        name = self.name_input.text()
        quantity_text = self.quantity_input.text()

        if not name:
            self.show_error_message('Введите название товара')
            return

        try:
            quantity = int(quantity_text)
        except ValueError:
            self.show_error_message('Введите корректное количество товара (целое число)')
            return

        now = datetime.now()
        date = now.strftime('%Y.%m.%d %H:%M')  # Формат даты и времени

        # Создаем объект товара
        self.created_product = Product(name, quantity, date)

        # Для примера, выводим информацию о созданном товаре
        print(f"Создан товар: {self.created_product.name}, Количество: {self.created_product.quantity}, Дата: {self.created_product.date}")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Ошибка')
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    ex = ProductForm()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
