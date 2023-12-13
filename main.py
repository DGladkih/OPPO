from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import cProfile

class ProductCreationError(Exception):
    """
    Класс исключения для ошибок создания товара.
    """
    pass

class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
    - name: str - Название товара.
    - quantity: int - Количество товара.
    - date: str - Дата создания товара.
    """

    def __init__(self, name, quantity, date):
        """
        Конструктор класса Product.

        Параметры:
        - name: str - Название товара.
        - quantity: int - Количество товара.
        - date: str - Дата создания товара.
        """
        self.name = name
        self.quantity = quantity
        self.date = date

class ProductDataHandler:
    """
    Класс для обработки данных товара.
    """

    @staticmethod
    def create_product(name, quantity):
        """
        Создает объект товара на основе введенных данных.

        Параметры:
        - name: str - Название товара.
        - quantity: str - Количество товара (в строковом формате).

        Возвращает:
        - created_product: Product - Объект товара, если создан успешно.
        """
        try:
            if not name:
                raise ProductCreationError('Введите название товара')

            quantity = int(quantity)

            now = datetime.now()
            date = now.strftime('%Y.%m.%d %H:%M')  # Формат даты и времени

            created_product = Product(name, quantity, date)
            return created_product

        except ValueError:
            raise ProductCreationError('Введите корректное количество товара (целое число)')

class ProductForm(QWidget):
    """
    Класс для создания формы создания товара.
    """

    def __init__(self):
        """
        Конструктор класса ProductForm.
        """
        super().__init__()
        self.init_ui()
        self.created_product = None  # Добавляем переменную для хранения созданного товара

    def init_ui(self):
        """
        Инициализация пользовательского интерфейса.
        """
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
        """
        Обработка создания товара.
        """
        name = self.name_input.text()
        quantity_text = self.quantity_input.text()

        try:
            created_product = ProductDataHandler.create_product(name, quantity_text)
            self.created_product = created_product
            if self.created_product:
                print(f"Создан товар: {self.created_product.name}, Количество: {self.created_product.quantity}, Дата: {self.created_product.date}")

        except ProductCreationError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        """
        Отображает окно с сообщением об ошибке.
        """
        msg = QMessageBox()
        msg.setWindowTitle('Ошибка')
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

if __name__ == '__main__':
    # Запуск профилирования
    profiler = cProfile.Profile()
    profiler.enable()

    # Ваш существующий код
    app = QApplication([])
    product_form = ProductForm()
    app.exec_()

    # Отключение профилирования и вывод результатов
    profiler.disable()
    profiler.print_stats(sort='cumtime')
