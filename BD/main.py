import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import raspisanie
import main_window
import doctor
import pacient
import priem



class Expample(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        



class Accidents(QtWidgets.QMainWindow,raspisanie.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        self.Sort.clicked.connect(self.SortAccidents)
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Raspisanie'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Raspisanie WHERE ID = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Raspisanie (Work,Name,Start_time,End_time) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def SortAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Raspisanie ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Raspisanie SET Work='{self.ChangeLine_1.text()}', Name='{self.ChangeLine_2.text()}', Start_time='{self.ChangeLine_3.text()}', End_time='{self.ChangeLine_4.text()}' WHERE ID='{self.ChangeLine.text()}'")


        self.connection.commit()
        self.connection.close()

class Drivers(QtWidgets.QMainWindow,doctor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)
        self.Sort.clicked.connect(self.SortDrivers) 
        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Doctor'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Doctor WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Doctor' ('Second_name', 'First_name', 'Last_name', 'Labour', 'Cabinet', 'Todolist') VALUES (?, ?, ?, ?, ?, ?)",
                       (self.AddLine.text(), self.AddLine_2.text(), self.AddLine_3.text(), self.AddLine_4.text(), self.AddLine_5.text(), self.AddLine_6.text()))
                           
        self.connection.commit()
        self.connection.close()

    def SortDrivers(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Doctor' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()
        
        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    def ChangeDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Doctor' SET Second_name='{self.AddLine_9.text()}', First_name='{self.AddLine_10.text()}', Last_name='{self.AddLine_11.text()}', Labour='{self.AddLine_12.text()}', Cabinet='{self.AddLine_13.text()}', Todolist='{self.AddLine_14.text()}' WHERE ID='{self.AddLine_8.text()}'")
        
        self.connection.commit()
        self.connection.close()

class Fuel(QtWidgets.QMainWindow,pacient.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)
        self.Sort.clicked.connect(self.SortFuel)
        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Pacient'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Pacient WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Pacient (Second_name,First_name,Last_name,Born,Adress,Phone,Problem) VALUES(?,?,?,?,?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text(),self.AddLine_6.text(),self.AddLine_7.text(),))
        self.connection.commit()
        self.connection.close()

    def SortFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Pacient ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Pacient SET Second_name='{self.AddLine_9.text()}', First_name='{self.AddLine_10.text()}', Last_name='{self.AddLine_11.text()}', Born='{self.AddLine_12.text()}', Adress='{self.AddLine_13.text()}', Phone='{self.AddLine_14.text()}', Problem='{self.AddLine_15.text()}' WHERE ID='{self.AddLine_8.text()}'")

        self.connection.commit()
        self.connection.close()


class Inspection(QtWidgets.QMainWindow,priem.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Sort.clicked.connect(self.SortInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Priem'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Priem WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def SortInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Priem ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def AddInspection(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Priem (Data_time,Start_time,Doctor,Human) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\KURSACH\\db_main.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Priem SET Data_time='{self.ChangeLine_1.text()}', Start_time='{self.ChangeLine_2.text()}', Doctor='{self.ChangeLine_3.text()}', Human='{self.ChangeLine_4.text()}' WHERE ID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.accidents = Accidents()
        self.drivers = Drivers()
        self.fuel = Fuel()
        self.inspection = Inspection()
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.drivers)
        self.stacked_widget.addWidget(self.fuel)
        self.stacked_widget.addWidget(self.inspection)
        
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.accidents.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_drivers)
        self.drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.fuel.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)
        
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_drivers(self):
        self.stacked_widget.setCurrentWidget(self.drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.fuel)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
