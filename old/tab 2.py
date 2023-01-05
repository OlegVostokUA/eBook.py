import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import parse_db, parse_column_db, add_n_to_db, parse_column_db2, parse_db_rozklad
import datetime, time
import pandas as pd

today = datetime.datetime.today().strftime("%d.%m.%Y")


header_lables = ['Найменування', 'од. виміру', 'кількість']
kg = 'кг'

class MainTab(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(MainTab, self).__init__()
		self.parent = parent
		self.rows = parse_db()
		self.name_lables = parse_column_db2()
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.tableWidget = QtWidgets.QTableWidget(0, 3)
		self.tableWidget.setHorizontalHeaderLabels(header_lables)# врем. переменная. может и нет
		#self.tableWidget.setVerticalHeaderLabels(header_lables)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)

	def func_connect(self):
		self.tableWidget.setRowCount(70) #len(self.rows)
		for row, items in enumerate(self.name_lables):
			self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(items[2])))
			self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(items[3])))
			self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(items[4])))
			self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(items[5])))
			self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem(str(items[6])))
			self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem(str(items[7])))
			self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem(str(items[8])))
			self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem(str(items[9])))
			self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem(str(items[10])))
			self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem(str(items[11])))
			self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem(str(items[12])))
			self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem(str(items[13])))
			self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem(str(items[14])))
			self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem(str(items[15])))
			self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem(str(items[16])))
			self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem(str(items[17])))
			self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem(str(items[18])))
			self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem(str(items[19])))
			self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem(str(items[20])))
			self.tableWidget.setItem(19, 0, QtWidgets.QTableWidgetItem(str(items[21])))
			self.tableWidget.setItem(20, 0, QtWidgets.QTableWidgetItem(str(items[22])))
			self.tableWidget.setItem(21, 0, QtWidgets.QTableWidgetItem(str(items[23])))
			self.tableWidget.setItem(22, 0, QtWidgets.QTableWidgetItem(str(items[24])))
			self.tableWidget.setItem(23, 0, QtWidgets.QTableWidgetItem(str(items[25])))
			self.tableWidget.setItem(24, 0, QtWidgets.QTableWidgetItem(str(items[26])))
			self.tableWidget.setItem(25, 0, QtWidgets.QTableWidgetItem(str(items[27])))
			self.tableWidget.setItem(26, 0, QtWidgets.QTableWidgetItem(str(items[28])))
			self.tableWidget.setItem(27, 0, QtWidgets.QTableWidgetItem(str(items[29])))
			self.tableWidget.setItem(28, 0, QtWidgets.QTableWidgetItem(str(items[30])))
			self.tableWidget.setItem(29, 0, QtWidgets.QTableWidgetItem(str(items[31])))
			self.tableWidget.setItem(30, 0, QtWidgets.QTableWidgetItem(str(items[32])))
			self.tableWidget.setItem(31, 0, QtWidgets.QTableWidgetItem(str(items[33])))
			self.tableWidget.setItem(32, 0, QtWidgets.QTableWidgetItem(str(items[34])))
			self.tableWidget.setItem(33, 0, QtWidgets.QTableWidgetItem(str(items[35])))
			self.tableWidget.setItem(34, 0, QtWidgets.QTableWidgetItem(str(items[36])))
			self.tableWidget.setItem(35, 0, QtWidgets.QTableWidgetItem(str(items[37])))
			self.tableWidget.setItem(36, 0, QtWidgets.QTableWidgetItem(str(items[38])))
			self.tableWidget.setItem(37, 0, QtWidgets.QTableWidgetItem(str(items[39])))
			self.tableWidget.setItem(38, 0, QtWidgets.QTableWidgetItem(str(items[40])))
			self.tableWidget.setItem(39, 0, QtWidgets.QTableWidgetItem(str(items[41])))
			self.tableWidget.setItem(40, 0, QtWidgets.QTableWidgetItem(str(items[42])))
			self.tableWidget.setItem(41, 0, QtWidgets.QTableWidgetItem(str(items[43])))
			self.tableWidget.setItem(42, 0, QtWidgets.QTableWidgetItem(str(items[44])))
			self.tableWidget.setItem(43, 0, QtWidgets.QTableWidgetItem(str(items[45])))
			self.tableWidget.setItem(44, 0, QtWidgets.QTableWidgetItem(str(items[46])))
			self.tableWidget.setItem(45, 0, QtWidgets.QTableWidgetItem(str(items[47])))
			self.tableWidget.setItem(46, 0, QtWidgets.QTableWidgetItem(str(items[48])))
			self.tableWidget.setItem(47, 0, QtWidgets.QTableWidgetItem(str(items[49])))
			self.tableWidget.setItem(48, 0, QtWidgets.QTableWidgetItem(str(items[50])))
			self.tableWidget.setItem(49, 0, QtWidgets.QTableWidgetItem(str(items[51])))
			self.tableWidget.setItem(50, 0, QtWidgets.QTableWidgetItem(str(items[52])))
			self.tableWidget.setItem(51, 0, QtWidgets.QTableWidgetItem(str(items[53])))
			self.tableWidget.setItem(52, 0, QtWidgets.QTableWidgetItem(str(items[54])))
			self.tableWidget.setItem(53, 0, QtWidgets.QTableWidgetItem(str(items[55])))
			self.tableWidget.setItem(54, 0, QtWidgets.QTableWidgetItem(str(items[56])))
			self.tableWidget.setItem(55, 0, QtWidgets.QTableWidgetItem(str(items[57])))
			self.tableWidget.setItem(56, 0, QtWidgets.QTableWidgetItem(str(items[58])))
			self.tableWidget.setItem(57, 0, QtWidgets.QTableWidgetItem(str(items[59])))
			self.tableWidget.setItem(58, 0, QtWidgets.QTableWidgetItem(str(items[60])))
			self.tableWidget.setItem(59, 0, QtWidgets.QTableWidgetItem(str(items[61])))
			self.tableWidget.setItem(60, 0, QtWidgets.QTableWidgetItem(str(items[62])))
			self.tableWidget.setItem(61, 0, QtWidgets.QTableWidgetItem(str(items[63])))
			self.tableWidget.setItem(62, 0, QtWidgets.QTableWidgetItem(str(items[64])))
			self.tableWidget.setItem(63, 0, QtWidgets.QTableWidgetItem(str(items[65])))
			self.tableWidget.setItem(64, 0, QtWidgets.QTableWidgetItem(str(items[66])))
			self.tableWidget.setItem(65, 0, QtWidgets.QTableWidgetItem(str(items[67])))
			self.tableWidget.setItem(66, 0, QtWidgets.QTableWidgetItem(str(items[68])))
			self.tableWidget.setItem(67, 0, QtWidgets.QTableWidgetItem(str(items[69])))
			self.tableWidget.setItem(68, 0, QtWidgets.QTableWidgetItem(str(items[70])))
			self.tableWidget.setItem(69, 0, QtWidgets.QTableWidgetItem(str(items[71])))

		for row in range(70):
			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(kg))

		for row, items in enumerate(self.rows):
			self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(items[2])))
			self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(items[3])))
			self.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(str(items[4])))
			self.tableWidget.setItem(3, 2, QtWidgets.QTableWidgetItem(str(items[5])))
			self.tableWidget.setItem(4, 2, QtWidgets.QTableWidgetItem(str(items[6])))
			self.tableWidget.setItem(5, 2, QtWidgets.QTableWidgetItem(str(items[7])))
			self.tableWidget.setItem(6, 2, QtWidgets.QTableWidgetItem(str(items[8])))
			self.tableWidget.setItem(7, 2, QtWidgets.QTableWidgetItem(str(items[9])))
			self.tableWidget.setItem(8, 2, QtWidgets.QTableWidgetItem(str(items[10])))
			self.tableWidget.setItem(9, 2, QtWidgets.QTableWidgetItem(str(items[11])))
			self.tableWidget.setItem(10, 2, QtWidgets.QTableWidgetItem(str(items[12])))
			self.tableWidget.setItem(11, 2, QtWidgets.QTableWidgetItem(str(items[13])))
			self.tableWidget.setItem(12, 2, QtWidgets.QTableWidgetItem(str(items[14])))
			self.tableWidget.setItem(13, 2, QtWidgets.QTableWidgetItem(str(items[15])))
			self.tableWidget.setItem(14, 2, QtWidgets.QTableWidgetItem(str(items[16])))
			self.tableWidget.setItem(15, 2, QtWidgets.QTableWidgetItem(str(items[17])))
			self.tableWidget.setItem(16, 2, QtWidgets.QTableWidgetItem(str(items[18])))
			self.tableWidget.setItem(17, 2, QtWidgets.QTableWidgetItem(str(items[19])))
			self.tableWidget.setItem(18, 2, QtWidgets.QTableWidgetItem(str(items[20])))
			self.tableWidget.setItem(19, 2, QtWidgets.QTableWidgetItem(str(items[21])))
			self.tableWidget.setItem(20, 2, QtWidgets.QTableWidgetItem(str(items[22])))
			self.tableWidget.setItem(21, 2, QtWidgets.QTableWidgetItem(str(items[23])))
			self.tableWidget.setItem(22, 2, QtWidgets.QTableWidgetItem(str(items[24])))
			self.tableWidget.setItem(23, 2, QtWidgets.QTableWidgetItem(str(items[25])))
			self.tableWidget.setItem(24, 2, QtWidgets.QTableWidgetItem(str(items[26])))
			self.tableWidget.setItem(25, 2, QtWidgets.QTableWidgetItem(str(items[27])))
			self.tableWidget.setItem(26, 2, QtWidgets.QTableWidgetItem(str(items[28])))
			self.tableWidget.setItem(27, 2, QtWidgets.QTableWidgetItem(str(items[29])))
			self.tableWidget.setItem(28, 2, QtWidgets.QTableWidgetItem(str(items[30])))
			self.tableWidget.setItem(29, 2, QtWidgets.QTableWidgetItem(str(items[31])))
			self.tableWidget.setItem(30, 2, QtWidgets.QTableWidgetItem(str(items[32])))
			self.tableWidget.setItem(31, 2, QtWidgets.QTableWidgetItem(str(items[33])))
			self.tableWidget.setItem(32, 2, QtWidgets.QTableWidgetItem(str(items[34])))
			self.tableWidget.setItem(33, 2, QtWidgets.QTableWidgetItem(str(items[35])))
			self.tableWidget.setItem(34, 2, QtWidgets.QTableWidgetItem(str(items[36])))
			self.tableWidget.setItem(35, 2, QtWidgets.QTableWidgetItem(str(items[37])))
			self.tableWidget.setItem(36, 2, QtWidgets.QTableWidgetItem(str(items[38])))
			self.tableWidget.setItem(37, 2, QtWidgets.QTableWidgetItem(str(items[39])))
			self.tableWidget.setItem(38, 2, QtWidgets.QTableWidgetItem(str(items[40])))
			self.tableWidget.setItem(39, 2, QtWidgets.QTableWidgetItem(str(items[41])))
			self.tableWidget.setItem(40, 2, QtWidgets.QTableWidgetItem(str(items[42])))
			self.tableWidget.setItem(41, 2, QtWidgets.QTableWidgetItem(str(items[43])))
			self.tableWidget.setItem(42, 2, QtWidgets.QTableWidgetItem(str(items[44])))
			self.tableWidget.setItem(43, 2, QtWidgets.QTableWidgetItem(str(items[45])))
			self.tableWidget.setItem(44, 2, QtWidgets.QTableWidgetItem(str(items[46])))
			self.tableWidget.setItem(45, 2, QtWidgets.QTableWidgetItem(str(items[47])))
			self.tableWidget.setItem(46, 2, QtWidgets.QTableWidgetItem(str(items[48])))
			self.tableWidget.setItem(47, 2, QtWidgets.QTableWidgetItem(str(items[49])))
			self.tableWidget.setItem(48, 2, QtWidgets.QTableWidgetItem(str(items[50])))
			self.tableWidget.setItem(49, 2, QtWidgets.QTableWidgetItem(str(items[51])))
			self.tableWidget.setItem(50, 2, QtWidgets.QTableWidgetItem(str(items[52])))
			self.tableWidget.setItem(51, 2, QtWidgets.QTableWidgetItem(str(items[53])))
			self.tableWidget.setItem(52, 2, QtWidgets.QTableWidgetItem(str(items[54])))
			self.tableWidget.setItem(53, 2, QtWidgets.QTableWidgetItem(str(items[55])))
			self.tableWidget.setItem(54, 2, QtWidgets.QTableWidgetItem(str(items[56])))
			self.tableWidget.setItem(55, 2, QtWidgets.QTableWidgetItem(str(items[57])))
			self.tableWidget.setItem(56, 2, QtWidgets.QTableWidgetItem(str(items[58])))
			self.tableWidget.setItem(57, 2, QtWidgets.QTableWidgetItem(str(items[59])))
			self.tableWidget.setItem(58, 2, QtWidgets.QTableWidgetItem(str(items[60])))
			self.tableWidget.setItem(59, 2, QtWidgets.QTableWidgetItem(str(items[61])))
			self.tableWidget.setItem(60, 2, QtWidgets.QTableWidgetItem(str(items[62])))
			self.tableWidget.setItem(61, 2, QtWidgets.QTableWidgetItem(str(items[63])))
			self.tableWidget.setItem(62, 2, QtWidgets.QTableWidgetItem(str(items[64])))
			self.tableWidget.setItem(63, 2, QtWidgets.QTableWidgetItem(str(items[65])))
			self.tableWidget.setItem(64, 2, QtWidgets.QTableWidgetItem(str(items[66])))
			self.tableWidget.setItem(65, 2, QtWidgets.QTableWidgetItem(str(items[67])))
			self.tableWidget.setItem(66, 2, QtWidgets.QTableWidgetItem(str(items[68])))
			self.tableWidget.setItem(67, 2, QtWidgets.QTableWidgetItem(str(items[69])))
			self.tableWidget.setItem(68, 2, QtWidgets.QTableWidgetItem(str(items[70])))
			self.tableWidget.setItem(69, 2, QtWidgets.QTableWidgetItem(str(items[71])))

    #self.func_connect()

class ProfitTab(QtWidgets.QWidget):
		
	def __init__(self, parent=None):
		super(ProfitTab, self).__init__()
		self.parent = parent
		self.rows = parse_db()
		self.name_lables = parse_column_db2()
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.pushButton2 = QtWidgets.QPushButton('Зберегти у Базу Даних')
		self.pushButton2.clicked.connect(self.push_to_db)
		self.pushButton3 = QtWidgets.QPushButton('Формувати у Excel')
		self.pushButton3.clicked.connect(self.exportToExcel)
		# button for Excel
		self.tableWidget = QtWidgets.QTableWidget(0, 3)
		self.tableWidget.setHorizontalHeaderLabels(header_lables)# врем. переменная. может и нет
		self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        
		self.label_date = QtWidgets.QLabel(self)
		self.label_date.setText('Введіть дату операції:')
		self.input_date = QtWidgets.QLineEdit(today)
        
		self.label_pidr = QtWidgets.QLabel(self)
		self.label_pidr.setText('Введіть назву постачальника або номер військової частини:')
		self.input_pidr = QtWidgets.QLineEdit(self)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.label_date)
		vbox.addWidget(self.input_date)
		vbox.addWidget(self.label_pidr)
		vbox.addWidget(self.input_pidr)
		#vbox.addWidget(self.label_name)
		#vbox.addWidget(self.input_name)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton2)
		vbox.addWidget(self.pushButton3)

	def func_connect(self):
		self.tableWidget.setRowCount(70) #len(self.rows)
		for row, items in enumerate(self.name_lables):
			self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(items[2])))
			self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(items[3])))
			self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(items[4])))
			self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(items[5])))
			self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem(str(items[6])))
			self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem(str(items[7])))
			self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem(str(items[8])))
			self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem(str(items[9])))
			self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem(str(items[10])))
			self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem(str(items[11])))
			self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem(str(items[12])))
			self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem(str(items[13])))
			self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem(str(items[14])))
			self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem(str(items[15])))
			self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem(str(items[16])))
			self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem(str(items[17])))
			self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem(str(items[18])))
			self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem(str(items[19])))
			self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem(str(items[20])))
			self.tableWidget.setItem(19, 0, QtWidgets.QTableWidgetItem(str(items[21])))
			self.tableWidget.setItem(20, 0, QtWidgets.QTableWidgetItem(str(items[22])))
			self.tableWidget.setItem(21, 0, QtWidgets.QTableWidgetItem(str(items[23])))
			self.tableWidget.setItem(22, 0, QtWidgets.QTableWidgetItem(str(items[24])))
			self.tableWidget.setItem(23, 0, QtWidgets.QTableWidgetItem(str(items[25])))
			self.tableWidget.setItem(24, 0, QtWidgets.QTableWidgetItem(str(items[26])))
			self.tableWidget.setItem(25, 0, QtWidgets.QTableWidgetItem(str(items[27])))
			self.tableWidget.setItem(26, 0, QtWidgets.QTableWidgetItem(str(items[28])))
			self.tableWidget.setItem(27, 0, QtWidgets.QTableWidgetItem(str(items[29])))
			self.tableWidget.setItem(28, 0, QtWidgets.QTableWidgetItem(str(items[30])))
			self.tableWidget.setItem(29, 0, QtWidgets.QTableWidgetItem(str(items[31])))
			self.tableWidget.setItem(30, 0, QtWidgets.QTableWidgetItem(str(items[32])))
			self.tableWidget.setItem(31, 0, QtWidgets.QTableWidgetItem(str(items[33])))
			self.tableWidget.setItem(32, 0, QtWidgets.QTableWidgetItem(str(items[34])))
			self.tableWidget.setItem(33, 0, QtWidgets.QTableWidgetItem(str(items[35])))
			self.tableWidget.setItem(34, 0, QtWidgets.QTableWidgetItem(str(items[36])))
			self.tableWidget.setItem(35, 0, QtWidgets.QTableWidgetItem(str(items[37])))
			self.tableWidget.setItem(36, 0, QtWidgets.QTableWidgetItem(str(items[38])))
			self.tableWidget.setItem(37, 0, QtWidgets.QTableWidgetItem(str(items[39])))
			self.tableWidget.setItem(38, 0, QtWidgets.QTableWidgetItem(str(items[40])))
			self.tableWidget.setItem(39, 0, QtWidgets.QTableWidgetItem(str(items[41])))
			self.tableWidget.setItem(40, 0, QtWidgets.QTableWidgetItem(str(items[42])))
			self.tableWidget.setItem(41, 0, QtWidgets.QTableWidgetItem(str(items[43])))
			self.tableWidget.setItem(42, 0, QtWidgets.QTableWidgetItem(str(items[44])))
			self.tableWidget.setItem(43, 0, QtWidgets.QTableWidgetItem(str(items[45])))
			self.tableWidget.setItem(44, 0, QtWidgets.QTableWidgetItem(str(items[46])))
			self.tableWidget.setItem(45, 0, QtWidgets.QTableWidgetItem(str(items[47])))
			self.tableWidget.setItem(46, 0, QtWidgets.QTableWidgetItem(str(items[48])))
			self.tableWidget.setItem(47, 0, QtWidgets.QTableWidgetItem(str(items[49])))
			self.tableWidget.setItem(48, 0, QtWidgets.QTableWidgetItem(str(items[50])))
			self.tableWidget.setItem(49, 0, QtWidgets.QTableWidgetItem(str(items[51])))
			self.tableWidget.setItem(50, 0, QtWidgets.QTableWidgetItem(str(items[52])))
			self.tableWidget.setItem(51, 0, QtWidgets.QTableWidgetItem(str(items[53])))
			self.tableWidget.setItem(52, 0, QtWidgets.QTableWidgetItem(str(items[54])))
			self.tableWidget.setItem(53, 0, QtWidgets.QTableWidgetItem(str(items[55])))
			self.tableWidget.setItem(54, 0, QtWidgets.QTableWidgetItem(str(items[56])))
			self.tableWidget.setItem(55, 0, QtWidgets.QTableWidgetItem(str(items[57])))
			self.tableWidget.setItem(56, 0, QtWidgets.QTableWidgetItem(str(items[58])))
			self.tableWidget.setItem(57, 0, QtWidgets.QTableWidgetItem(str(items[59])))
			self.tableWidget.setItem(58, 0, QtWidgets.QTableWidgetItem(str(items[60])))
			self.tableWidget.setItem(59, 0, QtWidgets.QTableWidgetItem(str(items[61])))
			self.tableWidget.setItem(60, 0, QtWidgets.QTableWidgetItem(str(items[62])))
			self.tableWidget.setItem(61, 0, QtWidgets.QTableWidgetItem(str(items[63])))
			self.tableWidget.setItem(62, 0, QtWidgets.QTableWidgetItem(str(items[64])))
			self.tableWidget.setItem(63, 0, QtWidgets.QTableWidgetItem(str(items[65])))
			self.tableWidget.setItem(64, 0, QtWidgets.QTableWidgetItem(str(items[66])))
			self.tableWidget.setItem(65, 0, QtWidgets.QTableWidgetItem(str(items[67])))
			self.tableWidget.setItem(66, 0, QtWidgets.QTableWidgetItem(str(items[68])))
			self.tableWidget.setItem(67, 0, QtWidgets.QTableWidgetItem(str(items[69])))
			self.tableWidget.setItem(68, 0, QtWidgets.QTableWidgetItem(str(items[70])))
			self.tableWidget.setItem(69, 0, QtWidgets.QTableWidgetItem(str(items[71])))

		for row in range(70):
			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(kg))


	def push_to_db(self):
		signal = 1
		date = self.input_date.text()
		item = self.input_pidr.text()
		item = int(item)
		date_op = (date,)
		number_ch = (item,)
		column = 2 #0 1
		data = []
		for row in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(row, column) is not None:
				item = self.tableWidget.item(row, column).text()
				item = int(item)
				#print(type(item))
			else:
				item = 0
			data.append(item)
			val_ch = tuple(data)
		add_n_to_db(signal, number_ch, date_op, val_ch) # and "data" on future
	
	def exportToExcel(self):
		timedate = time.ctime()
		name = self.input_pidr.text()
		timefile = timedate[4:10]
		formatfile = '.xlsx'
		file = name+'.'+timefile+formatfile
		#print(file)
		columnHeaders = []
		for j in range(self.tableWidget.model().columnCount()):
			columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
			df = pd.DataFrame(columns=columnHeaders)
		for row in range(self.tableWidget.rowCount()):
			for col in range(self.tableWidget.columnCount()):
				try:
					temp = self.tableWidget.item(row, col).text()
				except:
					temp = 0
				df.at[row, columnHeaders[col]] = temp
				df.to_excel(file)
    	           	

class LossTab(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super(LossTab, self).__init__()
		self.parent = parent
		self.rows = parse_db()
		self.name_lables = parse_column_db2()
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.pushButton2 = QtWidgets.QPushButton('Зберегти у Базу Даних')
		self.pushButton2.clicked.connect(self.push_to_db)
		self.pushButton3 = QtWidgets.QPushButton('Формувати у Excel')
		self.pushButton3.clicked.connect(self.exportToExcel)

		self.tableWidget = QtWidgets.QTableWidget(0, 3)
		self.tableWidget.setHorizontalHeaderLabels(header_lables)  # врем. переменная. может и нет
		self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

		self.label_date = QtWidgets.QLabel(self)
		self.label_date.setText('Введіть дату операції:')
		self.input_date = QtWidgets.QLineEdit(today)

		self.label_pidr = QtWidgets.QLabel(self)
		self.label_pidr.setText('Введіть назву підрозділу або номер військової частини:')
		self.input_pidr = QtWidgets.QLineEdit(self)

		self.label_name = QtWidgets.QLabel(self)
		self.label_name.setText('Введіть прізвище, ім’я того, через кого здійснюєтся операція:')
		self.input_name = QtWidgets.QLineEdit(self)

		# self.topbox.addWidget(self.label_pidr)
		# self.topbox.addWidget(self.input_pidr)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.label_date)
		vbox.addWidget(self.input_date)
		vbox.addWidget(self.label_pidr)
		vbox.addWidget(self.input_pidr)
		vbox.addWidget(self.label_name)
		vbox.addWidget(self.input_name)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton2)
		vbox.addWidget(self.pushButton3)

	def func_connect(self):
		self.tableWidget.setRowCount(70) #len(self.rows)
		for row, items in enumerate(self.name_lables):
			self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(items[2])))
			self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(items[3])))
			self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(items[4])))
			self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(items[5])))
			self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem(str(items[6])))
			self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem(str(items[7])))
			self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem(str(items[8])))
			self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem(str(items[9])))
			self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem(str(items[10])))
			self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem(str(items[11])))
			self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem(str(items[12])))
			self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem(str(items[13])))
			self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem(str(items[14])))
			self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem(str(items[15])))
			self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem(str(items[16])))
			self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem(str(items[17])))
			self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem(str(items[18])))
			self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem(str(items[19])))
			self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem(str(items[20])))
			self.tableWidget.setItem(19, 0, QtWidgets.QTableWidgetItem(str(items[21])))
			self.tableWidget.setItem(20, 0, QtWidgets.QTableWidgetItem(str(items[22])))
			self.tableWidget.setItem(21, 0, QtWidgets.QTableWidgetItem(str(items[23])))
			self.tableWidget.setItem(22, 0, QtWidgets.QTableWidgetItem(str(items[24])))
			self.tableWidget.setItem(23, 0, QtWidgets.QTableWidgetItem(str(items[25])))
			self.tableWidget.setItem(24, 0, QtWidgets.QTableWidgetItem(str(items[26])))
			self.tableWidget.setItem(25, 0, QtWidgets.QTableWidgetItem(str(items[27])))
			self.tableWidget.setItem(26, 0, QtWidgets.QTableWidgetItem(str(items[28])))
			self.tableWidget.setItem(27, 0, QtWidgets.QTableWidgetItem(str(items[29])))
			self.tableWidget.setItem(28, 0, QtWidgets.QTableWidgetItem(str(items[30])))
			self.tableWidget.setItem(29, 0, QtWidgets.QTableWidgetItem(str(items[31])))
			self.tableWidget.setItem(30, 0, QtWidgets.QTableWidgetItem(str(items[32])))
			self.tableWidget.setItem(31, 0, QtWidgets.QTableWidgetItem(str(items[33])))
			self.tableWidget.setItem(32, 0, QtWidgets.QTableWidgetItem(str(items[34])))
			self.tableWidget.setItem(33, 0, QtWidgets.QTableWidgetItem(str(items[35])))
			self.tableWidget.setItem(34, 0, QtWidgets.QTableWidgetItem(str(items[36])))
			self.tableWidget.setItem(35, 0, QtWidgets.QTableWidgetItem(str(items[37])))
			self.tableWidget.setItem(36, 0, QtWidgets.QTableWidgetItem(str(items[38])))
			self.tableWidget.setItem(37, 0, QtWidgets.QTableWidgetItem(str(items[39])))
			self.tableWidget.setItem(38, 0, QtWidgets.QTableWidgetItem(str(items[40])))
			self.tableWidget.setItem(39, 0, QtWidgets.QTableWidgetItem(str(items[41])))
			self.tableWidget.setItem(40, 0, QtWidgets.QTableWidgetItem(str(items[42])))
			self.tableWidget.setItem(41, 0, QtWidgets.QTableWidgetItem(str(items[43])))
			self.tableWidget.setItem(42, 0, QtWidgets.QTableWidgetItem(str(items[44])))
			self.tableWidget.setItem(43, 0, QtWidgets.QTableWidgetItem(str(items[45])))
			self.tableWidget.setItem(44, 0, QtWidgets.QTableWidgetItem(str(items[46])))
			self.tableWidget.setItem(45, 0, QtWidgets.QTableWidgetItem(str(items[47])))
			self.tableWidget.setItem(46, 0, QtWidgets.QTableWidgetItem(str(items[48])))
			self.tableWidget.setItem(47, 0, QtWidgets.QTableWidgetItem(str(items[49])))
			self.tableWidget.setItem(48, 0, QtWidgets.QTableWidgetItem(str(items[50])))
			self.tableWidget.setItem(49, 0, QtWidgets.QTableWidgetItem(str(items[51])))
			self.tableWidget.setItem(50, 0, QtWidgets.QTableWidgetItem(str(items[52])))
			self.tableWidget.setItem(51, 0, QtWidgets.QTableWidgetItem(str(items[53])))
			self.tableWidget.setItem(52, 0, QtWidgets.QTableWidgetItem(str(items[54])))
			self.tableWidget.setItem(53, 0, QtWidgets.QTableWidgetItem(str(items[55])))
			self.tableWidget.setItem(54, 0, QtWidgets.QTableWidgetItem(str(items[56])))
			self.tableWidget.setItem(55, 0, QtWidgets.QTableWidgetItem(str(items[57])))
			self.tableWidget.setItem(56, 0, QtWidgets.QTableWidgetItem(str(items[58])))
			self.tableWidget.setItem(57, 0, QtWidgets.QTableWidgetItem(str(items[59])))
			self.tableWidget.setItem(58, 0, QtWidgets.QTableWidgetItem(str(items[60])))
			self.tableWidget.setItem(59, 0, QtWidgets.QTableWidgetItem(str(items[61])))
			self.tableWidget.setItem(60, 0, QtWidgets.QTableWidgetItem(str(items[62])))
			self.tableWidget.setItem(61, 0, QtWidgets.QTableWidgetItem(str(items[63])))
			self.tableWidget.setItem(62, 0, QtWidgets.QTableWidgetItem(str(items[64])))
			self.tableWidget.setItem(63, 0, QtWidgets.QTableWidgetItem(str(items[65])))
			self.tableWidget.setItem(64, 0, QtWidgets.QTableWidgetItem(str(items[66])))
			self.tableWidget.setItem(65, 0, QtWidgets.QTableWidgetItem(str(items[67])))
			self.tableWidget.setItem(66, 0, QtWidgets.QTableWidgetItem(str(items[68])))
			self.tableWidget.setItem(67, 0, QtWidgets.QTableWidgetItem(str(items[69])))
			self.tableWidget.setItem(68, 0, QtWidgets.QTableWidgetItem(str(items[70])))
			self.tableWidget.setItem(69, 0, QtWidgets.QTableWidgetItem(str(items[71])))

		for row in range(70):
			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(kg))


	def push_to_db(self):
		signal = 2
		date = self.input_date.text()
		item = self.input_pidr.text()
		date_op = (date,)
		item = int(item)
		number_ch = (item,)
		column = 2  # 0 1
		data = []
		for row in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(row, column) is not None:
				item = self.tableWidget.item(row, column).text()
				item = int(item)
				#print(type(item))
			else:
				item = 0
			data.append(item)
			val_ch = tuple(data)
		add_n_to_db(signal, number_ch, date_op, val_ch) # and "data" on future

	def exportToExcel(self):
		timedate = time.ctime()
		name = self.input_pidr.text()
		timefile = timedate[4:10]
		formatfile = '.xlsx'
		file = name+'.'+timefile+formatfile
		#print(file)
		columnHeaders = []
		for j in range(self.tableWidget.model().columnCount()):
			columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
			df = pd.DataFrame(columns=columnHeaders)
		for row in range(self.tableWidget.rowCount()):
			for col in range(self.tableWidget.columnCount()):
				try:
					temp = self.tableWidget.item(row, col).text()
					temp = float(temp)
				except:
					temp = 0
					temp = float(temp)
				df.at[row, columnHeaders[col]] = temp
				df.to_excel(file)

rows = ('1', '2', '3', '4')
colums = ('День тижня', 'Прийом їжі', 'Страва', 'Хліб')


class Rozkladka(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super(Rozkladka, self).__init__()
		self.parent = parent
		self.rows = parse_db_rozklad()
		#print(self.rows)
		self.name_lables_main = colums
		self.name_lables_one = parse_column_db2()
		self.name_lables = self.name_lables_one[0]
		self.name_lables = self.name_lables[2:]
		self.names_columns = self.name_lables_main+self.name_lables
		#print(self.names_columns)
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.pushButton2 = QtWidgets.QPushButton('Зберегти у Базу Даних')
		#self.pushButton2.clicked.connect(self.push_to_db)

		self.tableWidget = QtWidgets.QTableWidget(0, 74)
		self.tableWidget.setHorizontalHeaderLabels(self.names_columns)  # врем. переменная. может и нет
		self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton2)


	def func_connect(self):
		self.tableWidget.setRowCount(70) #len(self.rows)
		for i in self.rows:
			val = []
			temp = i
			val.append(temp)
			for j in temp: #for j, items in enumerate(val):
				print(j)
				self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(temp[0]))
				self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(temp[1]))

"""
		for row, items in enumerate(self.rows):
			self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(items[0])))
			self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(items[1])))
			self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(items[2])))
			self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(items[3])))
"""





class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.tab1 = QtWidgets.QTabWidget()
		#self.tab1.setTabPosition(QtWidgets.QTabWidget.West)
		#self.tab1.setMovable(True)
		self.setCentralWidget(self.tab1)
        
		self.tab1.addTab(MainTab(), 'Залишки склад')
		#self.func_connect()
		self.tab1.addTab(ProfitTab(), 'Прихід')
		#self.func_connect()
		self.tab1.addTab(LossTab(), 'Розхід')

		self.tab1.addTab(Rozkladka(), 'Розкладка')




if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
	win = MyWindow()
	win.resize(1020, 960)
	win.show()
	sys.exit(app.exec_())

