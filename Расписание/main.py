import gspread
from abc import ABC , abstractmethod
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://docs.google.com/spreadsheets/d/1y-SS5WmtOUdv-il7sFa7HqvSDfflRE5NknjBOP1S-Rk/edit?gid=1451996418#gid=1451996418"]

#Абстрактный класс для работы с таблице расписания
class ScheduleTable(ABC):
    @abstractmethod
    def load(self):
        pass
#Уласс для загрузки гугл таблицы
class ScheduleTableGoogle(ScheduleTable):
    def load(self):
        pass
    def test(self):
        pass