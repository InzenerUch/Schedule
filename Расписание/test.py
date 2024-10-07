import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys
from PyQt6.QtWidgets import QApplication, QWidget,QTableWidget,QTableWidgetItem, QVBoxLayout, QMainWindow
import datetime
#Класс таблицы
class MyTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
    def setDate(self,data):
        for i in range(len(data)):
            self.insertRow(self.rowCount())
            for j in range(3):
                item = QTableWidgetItem(str(data[i][j]))
                self.setItem(self.rowCount()-1,j,item)

current_date = str(datetime.datetime.now().day+2) + "/" + str(datetime.datetime.now().month)
print(current_date)
#Регулярное выражение 
pattern_date = re.compile(".*"+ "(" + current_date + ")" +".*")
pattern_group = re.compile("(?=.*М-124-2.*)")
# Определяем область доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Загружаем учетные данные
creds = ServiceAccountCredentials.from_json_keyfile_name('schedule-436807-a04789d9d99d.json', scope)

# Авторизуемся и создаем клиент
client = gspread.authorize(creds)

# Открытие таблицы по ссылке
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1y-SS5WmtOUdv-il7sFa7HqvSDfflRE5NknjBOP1S-Rk/edit?gid=1451996418#gid=1451996418')
# Создание новой таблицы
# cell = worksheet.find(search_string)
sheet = spreadsheet.worksheet("Магистратура")
cell_group = sheet.find(pattern_group)
cell_date = sheet.find(pattern_date)
cell_list = [sheet.range(cell_date.row+i,cell_group.col,cell_date.row+i,cell_group.col+2) for i in range(7)]
print(cell_list)
values = [[i.value for i in cell ] for cell in cell_list]
print(values)

# create the QApplication
app = QApplication(sys.argv)

table = MyTable()
table.setColumnCount(3)
tableHeaders = ["Предмет", "Преподаватель", "Кабинет"] # Заголовки столбцов
table.setHorizontalHeaderLabels(tableHeaders)
table.setDate(values)
table.resizeColumnsToContents()
# create the main window
window = QMainWindow(windowTitle='Hello World')
window.setCentralWidget(table)
window.show()

# start the event loop
app.exec()
# for i in range(7):
#     cell_notation = gspread.utils.rowcol_to_a1(cell_date.row+i, cell_group.col)
#     value = sheet.acell(cell_notation).value
#     print("Строка найдена в {}".format(cell_notation))
#     print("Значение ячейки {}".format(str(cell_notation)) + " = " + str(value))
