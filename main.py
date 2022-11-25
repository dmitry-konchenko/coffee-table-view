import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from sqlite3 import connect
from PyQt5.QtWidgets import (
    QMainWindow,
    QTableWidgetItem,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('coffee_search.ui', self)
        self._connection = connect('coffee.sqlite')
        self._init_ui()

    def _init_ui(self) -> None:
        cursor = self._connection.cursor()
        result = cursor.execute(f'''
            SELECT * FROM coffee
        ''')
        coffee = result.fetchall()
        self._show_coffee(coffee)

    def _show_coffee(self, coffee_items: list[tuple[str, int]]) -> None:
        self.tableWidget.setRowCount(len(coffee_items))
        self.tableWidget.setColumnCount(len(coffee_items[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "название сорта", "степень обжарки", "молотый/в зернах",
                                                  "описание вкуса", "цена", "объем упаковки"])
        for i, film in enumerate(coffee_items):
            for j, val in enumerate(film):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
exit_code = app.exec()
sys.exit(exit_code)
