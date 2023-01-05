import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import parse_db, \
	add_n_to_db, \
	parse_column_db2, \
	parse_db_rozklad, \
	clear_rozclad_db, \
	add_values_to_rozclad_db, \
	parse_day_rozklad, \
	parse_day_dinner_rozklad
import datetime, time
import pandas as pd

today = datetime.datetime.today().strftime("%d.%m.%Y")
day_of_week = datetime.datetime.today().isoweekday()


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
		self.tableWidget.setHorizontalHeaderLabels(header_lables)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(300)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)

	def func_connect(self):
		self.tableWidget.setRowCount(70)
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
		self.tableWidget = QtWidgets.QTableWidget(0, 3)
		self.tableWidget.setHorizontalHeaderLabels(header_lables)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
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
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton2)
		vbox.addWidget(self.pushButton3)

	def func_connect(self):
		self.tableWidget.setRowCount(70)
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
		column = 2
		data = []
		for row in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(row, column) is not None:
				item = self.tableWidget.item(row, column).text()
				item = int(item)
			else:
				item = 0
			data.append(item)
			val_ch = tuple(data)
		add_n_to_db(signal, number_ch, date_op, val_ch)
	
	def exportToExcel(self):
		timedate = time.ctime()
		name = self.input_pidr.text()
		timefile = timedate[4:10]
		formatfile = '.xlsx'
		file = name+'.'+timefile+formatfile
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
		self.tableWidget.setHorizontalHeaderLabels(header_lables)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(300)

		self.label_date = QtWidgets.QLabel(self)
		self.label_date.setText('Введіть дату операції:')
		self.input_date = QtWidgets.QLineEdit(today)

		self.label_pidr = QtWidgets.QLabel(self)
		self.label_pidr.setText('Введіть назву підрозділу або номер військової частини:')
		self.input_pidr = QtWidgets.QLineEdit(self)

		self.label_name = QtWidgets.QLabel(self)
		self.label_name.setText('Введіть прізвище, ім’я того, через кого здійснюєтся операція:')
		self.input_name = QtWidgets.QLineEdit(self)

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
		self.tableWidget.setRowCount(70)
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
		column = 2
		data = []
		for row in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(row, column) is not None:
				item = self.tableWidget.item(row, column).text()
				item = int(item)
			else:
				item = 0
			data.append(item)
			val_ch = tuple(data)
		add_n_to_db(signal, number_ch, date_op, val_ch)

	def exportToExcel(self):
		timedate = time.ctime()
		name = self.input_pidr.text()
		timefile = timedate[4:10]
		formatfile = '.xlsx'
		file = name+'.'+timefile+formatfile
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


colums = ('День тижня', 'Прийом їжі', 'Страва', 'Хліб')


class Rozkladka(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super(Rozkladka, self).__init__()
		self.parent = parent
		self.rows = parse_db_rozklad()
		self.name_lables_main = colums
		self.name_lables_one = parse_column_db2()
		self.name_lables = self.name_lables_one[0]
		self.name_lables = self.name_lables[2:]
		self.names_columns = self.name_lables_main+self.name_lables
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.pushButton2 = QtWidgets.QPushButton('Зберегти у Базу Даних')
		self.pushButton2.clicked.connect(self.delete_from_rozclad)
		self.pushButton2.clicked.connect(self.push_to_db)

		self.tableWidget = QtWidgets.QTableWidget(0, 74)
		self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(120)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton2)

	def delete_from_rozclad(self):

		clear_rozclad_db()

	def func_connect(self):
		self.tableWidget.setRowCount(65)
		row = -1
		count = 0
		for i in self.rows:
			temp = i
			count = count+1
			row = row+1
			for j in temp:
				self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(temp[0]))
				self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(temp[1]))
				self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(temp[2]))
				self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(temp[3])))
				self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(temp[4])))
				self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(temp[5])))
				self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(temp[6])))
				self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(temp[7])))
				self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(temp[8])))
				self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(temp[9])))
				self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(temp[10])))
				self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(temp[11])))
				self.tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(str(temp[12])))
				self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(temp[13])))
				self.tableWidget.setItem(row, 14, QtWidgets.QTableWidgetItem(str(temp[14])))
				self.tableWidget.setItem(row, 15, QtWidgets.QTableWidgetItem(str(temp[15])))
				self.tableWidget.setItem(row, 16, QtWidgets.QTableWidgetItem(str(temp[16])))
				self.tableWidget.setItem(row, 17, QtWidgets.QTableWidgetItem(str(temp[17])))
				self.tableWidget.setItem(row, 18, QtWidgets.QTableWidgetItem(str(temp[18])))
				self.tableWidget.setItem(row, 19, QtWidgets.QTableWidgetItem(str(temp[19])))
				self.tableWidget.setItem(row, 20, QtWidgets.QTableWidgetItem(str(temp[20])))
				self.tableWidget.setItem(row, 21, QtWidgets.QTableWidgetItem(str(temp[21])))
				self.tableWidget.setItem(row, 22, QtWidgets.QTableWidgetItem(str(temp[22])))
				self.tableWidget.setItem(row, 23, QtWidgets.QTableWidgetItem(str(temp[23])))
				self.tableWidget.setItem(row, 24, QtWidgets.QTableWidgetItem(str(temp[24])))
				self.tableWidget.setItem(row, 25, QtWidgets.QTableWidgetItem(str(temp[25])))
				self.tableWidget.setItem(row, 26, QtWidgets.QTableWidgetItem(str(temp[26])))
				self.tableWidget.setItem(row, 27, QtWidgets.QTableWidgetItem(str(temp[27])))
				self.tableWidget.setItem(row, 28, QtWidgets.QTableWidgetItem(str(temp[28])))
				self.tableWidget.setItem(row, 29, QtWidgets.QTableWidgetItem(str(temp[29])))
				self.tableWidget.setItem(row, 30, QtWidgets.QTableWidgetItem(str(temp[30])))
				self.tableWidget.setItem(row, 31, QtWidgets.QTableWidgetItem(str(temp[31])))
				self.tableWidget.setItem(row, 32, QtWidgets.QTableWidgetItem(str(temp[32])))
				self.tableWidget.setItem(row, 33, QtWidgets.QTableWidgetItem(str(temp[33])))
				self.tableWidget.setItem(row, 34, QtWidgets.QTableWidgetItem(str(temp[34])))
				self.tableWidget.setItem(row, 35, QtWidgets.QTableWidgetItem(str(temp[35])))
				self.tableWidget.setItem(row, 36, QtWidgets.QTableWidgetItem(str(temp[36])))
				self.tableWidget.setItem(row, 37, QtWidgets.QTableWidgetItem(str(temp[37])))
				self.tableWidget.setItem(row, 38, QtWidgets.QTableWidgetItem(str(temp[38])))
				self.tableWidget.setItem(row, 39, QtWidgets.QTableWidgetItem(str(temp[39])))
				self.tableWidget.setItem(row, 40, QtWidgets.QTableWidgetItem(str(temp[40])))
				self.tableWidget.setItem(row, 41, QtWidgets.QTableWidgetItem(str(temp[41])))
				self.tableWidget.setItem(row, 42, QtWidgets.QTableWidgetItem(str(temp[42])))
				self.tableWidget.setItem(row, 43, QtWidgets.QTableWidgetItem(str(temp[43])))
				self.tableWidget.setItem(row, 44, QtWidgets.QTableWidgetItem(str(temp[44])))
				self.tableWidget.setItem(row, 45, QtWidgets.QTableWidgetItem(str(temp[45])))
				self.tableWidget.setItem(row, 46, QtWidgets.QTableWidgetItem(str(temp[46])))
				self.tableWidget.setItem(row, 47, QtWidgets.QTableWidgetItem(str(temp[47])))
				self.tableWidget.setItem(row, 48, QtWidgets.QTableWidgetItem(str(temp[48])))
				self.tableWidget.setItem(row, 49, QtWidgets.QTableWidgetItem(str(temp[49])))
				self.tableWidget.setItem(row, 50, QtWidgets.QTableWidgetItem(str(temp[50])))
				self.tableWidget.setItem(row, 51, QtWidgets.QTableWidgetItem(str(temp[51])))
				self.tableWidget.setItem(row, 52, QtWidgets.QTableWidgetItem(str(temp[52])))
				self.tableWidget.setItem(row, 53, QtWidgets.QTableWidgetItem(str(temp[53])))
				self.tableWidget.setItem(row, 54, QtWidgets.QTableWidgetItem(str(temp[54])))
				self.tableWidget.setItem(row, 55, QtWidgets.QTableWidgetItem(str(temp[55])))
				self.tableWidget.setItem(row, 56, QtWidgets.QTableWidgetItem(str(temp[56])))
				self.tableWidget.setItem(row, 57, QtWidgets.QTableWidgetItem(str(temp[57])))
				self.tableWidget.setItem(row, 58, QtWidgets.QTableWidgetItem(str(temp[58])))
				self.tableWidget.setItem(row, 59, QtWidgets.QTableWidgetItem(str(temp[59])))
				self.tableWidget.setItem(row, 60, QtWidgets.QTableWidgetItem(str(temp[60])))
				self.tableWidget.setItem(row, 61, QtWidgets.QTableWidgetItem(str(temp[61])))
				self.tableWidget.setItem(row, 62, QtWidgets.QTableWidgetItem(str(temp[62])))
				self.tableWidget.setItem(row, 63, QtWidgets.QTableWidgetItem(str(temp[63])))
				self.tableWidget.setItem(row, 64, QtWidgets.QTableWidgetItem(str(temp[64])))
				self.tableWidget.setItem(row, 65, QtWidgets.QTableWidgetItem(str(temp[65])))
				self.tableWidget.setItem(row, 66, QtWidgets.QTableWidgetItem(str(temp[66])))
				self.tableWidget.setItem(row, 67, QtWidgets.QTableWidgetItem(str(temp[67])))
				self.tableWidget.setItem(row, 68, QtWidgets.QTableWidgetItem(str(temp[68])))
				self.tableWidget.setItem(row, 69, QtWidgets.QTableWidgetItem(str(temp[69])))
				self.tableWidget.setItem(row, 70, QtWidgets.QTableWidgetItem(str(temp[70])))
				self.tableWidget.setItem(row, 71, QtWidgets.QTableWidgetItem(str(temp[71])))
				self.tableWidget.setItem(row, 72, QtWidgets.QTableWidgetItem(str(temp[72])))
				self.tableWidget.setItem(row, 73, QtWidgets.QTableWidgetItem(str(temp[73])))

	def push_to_db(self):
		for row in range(self.tableWidget.rowCount()):
			data = []
			for coll in range(self.tableWidget.columnCount()):
				if self.tableWidget.item(row, coll) is not None:
					item = self.tableWidget.item(row, coll).text()
				else:
					item = 0
					item = str(item)
				data.append(item)
			val_roz = tuple(data)
			add_values_to_rozclad_db(val_roz)


class Menu(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super(Menu, self).__init__()
		self.parent = parent
		self.name_lables_main = colums
		self.name_lables_one = parse_column_db2()
		self.name_lables = self.name_lables_one[0]
		self.name_lables = self.name_lables[2:]
		self.names_columns = self.name_lables_main+self.name_lables
		self.pushButton = QtWidgets.QPushButton('Сформувати таблицю')
		self.pushButton.clicked.connect(self.func_connect)
		self.pushButton3 = QtWidgets.QPushButton('Провести розрахунок')
		self.pushButton3.clicked.connect(self.calculate)
		self.pushButton2 = QtWidgets.QPushButton('Зберегти у Базу Даних')
		self.pushButton2.clicked.connect(self.push_to_db)
		self.pushButton4 = QtWidgets.QPushButton('Формувати у Excel')
		self.pushButton4.clicked.connect(self.exportToExcel)

		self.tableWidget = QtWidgets.QTableWidget(0, 74)
		self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(120)

		self.tableWidget2 = QtWidgets.QTableWidget(0, 74)
		self.tableWidget2.setHorizontalHeaderLabels(self.names_columns)
		self.tableWidget2.horizontalHeader().setDefaultSectionSize(120)

		self.label_date = QtWidgets.QLabel(self)
		self.label_date.setText('Введіть дату операції:')
		self.input_date = QtWidgets.QLineEdit(today)

		self.label_ppl = QtWidgets.QLabel(self)
		self.label_ppl.setText('Введіть кількість людей:')
		self.input_ppl = QtWidgets.QLineEdit(self)

		self.label_ppl_d = QtWidgets.QLabel(self)
		self.label_ppl_d.setText('Введіть кількість людей на обід:')
		self.input_ppl_d = QtWidgets.QLineEdit(self)

		self.label_day = QtWidgets.QLabel(self)
		self.label_day.setText('Введіть день тижня:')
		self.input_day = QtWidgets.QLineEdit(self)

		vbox = QtWidgets.QVBoxLayout(self)
		vbox.addWidget(self.label_date)
		vbox.addWidget(self.input_date)
		vbox.addWidget(self.label_ppl)
		vbox.addWidget(self.input_ppl)
		vbox.addWidget(self.label_ppl_d)
		vbox.addWidget(self.input_ppl_d)
		vbox.addWidget(self.label_day)
		vbox.addWidget(self.input_day)
		vbox.addWidget(self.tableWidget)
		vbox.addWidget(self.tableWidget2)
		vbox.addWidget(self.pushButton)
		vbox.addWidget(self.pushButton3)
		vbox.addWidget(self.pushButton2)
		vbox.addWidget(self.pushButton4)

	def func_connect(self):
		self.tableWidget.setRowCount(11)
		self.tableWidget2.setRowCount(5)
		day = self.input_day.text()
		day = (day,)
		self.rows = parse_day_rozklad(day)
		self.rows_dinner = parse_day_dinner_rozklad(day)
		row = -1
		count = 0
		for i in self.rows:
			temp = i
			count = count+1
			row = row+1
			for j in temp:
				self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(temp[0]))
				self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(temp[1]))
				self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(temp[2]))
				self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(temp[3])))
				self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(temp[4])))
				self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(temp[5])))
				self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(temp[6])))
				self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(temp[7])))
				self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(temp[8])))
				self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(temp[9])))
				self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(temp[10])))
				self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(temp[11])))
				self.tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(str(temp[12])))
				self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(temp[13])))
				self.tableWidget.setItem(row, 14, QtWidgets.QTableWidgetItem(str(temp[14])))
				self.tableWidget.setItem(row, 15, QtWidgets.QTableWidgetItem(str(temp[15])))
				self.tableWidget.setItem(row, 16, QtWidgets.QTableWidgetItem(str(temp[16])))
				self.tableWidget.setItem(row, 17, QtWidgets.QTableWidgetItem(str(temp[17])))
				self.tableWidget.setItem(row, 18, QtWidgets.QTableWidgetItem(str(temp[18])))
				self.tableWidget.setItem(row, 19, QtWidgets.QTableWidgetItem(str(temp[19])))
				self.tableWidget.setItem(row, 20, QtWidgets.QTableWidgetItem(str(temp[20])))
				self.tableWidget.setItem(row, 21, QtWidgets.QTableWidgetItem(str(temp[21])))
				self.tableWidget.setItem(row, 22, QtWidgets.QTableWidgetItem(str(temp[22])))
				self.tableWidget.setItem(row, 23, QtWidgets.QTableWidgetItem(str(temp[23])))
				self.tableWidget.setItem(row, 24, QtWidgets.QTableWidgetItem(str(temp[24])))
				self.tableWidget.setItem(row, 25, QtWidgets.QTableWidgetItem(str(temp[25])))
				self.tableWidget.setItem(row, 26, QtWidgets.QTableWidgetItem(str(temp[26])))
				self.tableWidget.setItem(row, 27, QtWidgets.QTableWidgetItem(str(temp[27])))
				self.tableWidget.setItem(row, 28, QtWidgets.QTableWidgetItem(str(temp[28])))
				self.tableWidget.setItem(row, 29, QtWidgets.QTableWidgetItem(str(temp[29])))
				self.tableWidget.setItem(row, 30, QtWidgets.QTableWidgetItem(str(temp[30])))
				self.tableWidget.setItem(row, 31, QtWidgets.QTableWidgetItem(str(temp[31])))
				self.tableWidget.setItem(row, 32, QtWidgets.QTableWidgetItem(str(temp[32])))
				self.tableWidget.setItem(row, 33, QtWidgets.QTableWidgetItem(str(temp[33])))
				self.tableWidget.setItem(row, 34, QtWidgets.QTableWidgetItem(str(temp[34])))
				self.tableWidget.setItem(row, 35, QtWidgets.QTableWidgetItem(str(temp[35])))
				self.tableWidget.setItem(row, 36, QtWidgets.QTableWidgetItem(str(temp[36])))
				self.tableWidget.setItem(row, 37, QtWidgets.QTableWidgetItem(str(temp[37])))
				self.tableWidget.setItem(row, 38, QtWidgets.QTableWidgetItem(str(temp[38])))
				self.tableWidget.setItem(row, 39, QtWidgets.QTableWidgetItem(str(temp[39])))
				self.tableWidget.setItem(row, 40, QtWidgets.QTableWidgetItem(str(temp[40])))
				self.tableWidget.setItem(row, 41, QtWidgets.QTableWidgetItem(str(temp[41])))
				self.tableWidget.setItem(row, 42, QtWidgets.QTableWidgetItem(str(temp[42])))
				self.tableWidget.setItem(row, 43, QtWidgets.QTableWidgetItem(str(temp[43])))
				self.tableWidget.setItem(row, 44, QtWidgets.QTableWidgetItem(str(temp[44])))
				self.tableWidget.setItem(row, 45, QtWidgets.QTableWidgetItem(str(temp[45])))
				self.tableWidget.setItem(row, 46, QtWidgets.QTableWidgetItem(str(temp[46])))
				self.tableWidget.setItem(row, 47, QtWidgets.QTableWidgetItem(str(temp[47])))
				self.tableWidget.setItem(row, 48, QtWidgets.QTableWidgetItem(str(temp[48])))
				self.tableWidget.setItem(row, 49, QtWidgets.QTableWidgetItem(str(temp[49])))
				self.tableWidget.setItem(row, 50, QtWidgets.QTableWidgetItem(str(temp[50])))
				self.tableWidget.setItem(row, 51, QtWidgets.QTableWidgetItem(str(temp[51])))
				self.tableWidget.setItem(row, 52, QtWidgets.QTableWidgetItem(str(temp[52])))
				self.tableWidget.setItem(row, 53, QtWidgets.QTableWidgetItem(str(temp[53])))
				self.tableWidget.setItem(row, 54, QtWidgets.QTableWidgetItem(str(temp[54])))
				self.tableWidget.setItem(row, 55, QtWidgets.QTableWidgetItem(str(temp[55])))
				self.tableWidget.setItem(row, 56, QtWidgets.QTableWidgetItem(str(temp[56])))
				self.tableWidget.setItem(row, 57, QtWidgets.QTableWidgetItem(str(temp[57])))
				self.tableWidget.setItem(row, 58, QtWidgets.QTableWidgetItem(str(temp[58])))
				self.tableWidget.setItem(row, 59, QtWidgets.QTableWidgetItem(str(temp[59])))
				self.tableWidget.setItem(row, 60, QtWidgets.QTableWidgetItem(str(temp[60])))
				self.tableWidget.setItem(row, 61, QtWidgets.QTableWidgetItem(str(temp[61])))
				self.tableWidget.setItem(row, 62, QtWidgets.QTableWidgetItem(str(temp[62])))
				self.tableWidget.setItem(row, 63, QtWidgets.QTableWidgetItem(str(temp[63])))
				self.tableWidget.setItem(row, 64, QtWidgets.QTableWidgetItem(str(temp[64])))
				self.tableWidget.setItem(row, 65, QtWidgets.QTableWidgetItem(str(temp[65])))
				self.tableWidget.setItem(row, 66, QtWidgets.QTableWidgetItem(str(temp[66])))
				self.tableWidget.setItem(row, 67, QtWidgets.QTableWidgetItem(str(temp[67])))
				self.tableWidget.setItem(row, 68, QtWidgets.QTableWidgetItem(str(temp[68])))
				self.tableWidget.setItem(row, 69, QtWidgets.QTableWidgetItem(str(temp[69])))
				self.tableWidget.setItem(row, 70, QtWidgets.QTableWidgetItem(str(temp[70])))
				self.tableWidget.setItem(row, 71, QtWidgets.QTableWidgetItem(str(temp[71])))
				self.tableWidget.setItem(row, 72, QtWidgets.QTableWidgetItem(str(temp[72])))
				self.tableWidget.setItem(row, 73, QtWidgets.QTableWidgetItem(str(temp[73])))

		row = -1
		count = 0
		for i in self.rows_dinner:
			temp = i
			count = count+1
			row = row+1
			for j in temp:
				self.tableWidget2.setItem(row, 0, QtWidgets.QTableWidgetItem(temp[0]))
				self.tableWidget2.setItem(row, 1, QtWidgets.QTableWidgetItem(temp[1]))
				self.tableWidget2.setItem(row, 2, QtWidgets.QTableWidgetItem(temp[2]))
				self.tableWidget2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(temp[3])))
				self.tableWidget2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(temp[4])))
				self.tableWidget2.setItem(row, 5, QtWidgets.QTableWidgetItem(str(temp[5])))
				self.tableWidget2.setItem(row, 6, QtWidgets.QTableWidgetItem(str(temp[6])))
				self.tableWidget2.setItem(row, 7, QtWidgets.QTableWidgetItem(str(temp[7])))
				self.tableWidget2.setItem(row, 8, QtWidgets.QTableWidgetItem(str(temp[8])))
				self.tableWidget2.setItem(row, 9, QtWidgets.QTableWidgetItem(str(temp[9])))
				self.tableWidget2.setItem(row, 10, QtWidgets.QTableWidgetItem(str(temp[10])))
				self.tableWidget2.setItem(row, 11, QtWidgets.QTableWidgetItem(str(temp[11])))
				self.tableWidget2.setItem(row, 12, QtWidgets.QTableWidgetItem(str(temp[12])))
				self.tableWidget2.setItem(row, 13, QtWidgets.QTableWidgetItem(str(temp[13])))
				self.tableWidget2.setItem(row, 14, QtWidgets.QTableWidgetItem(str(temp[14])))
				self.tableWidget2.setItem(row, 15, QtWidgets.QTableWidgetItem(str(temp[15])))
				self.tableWidget2.setItem(row, 16, QtWidgets.QTableWidgetItem(str(temp[16])))
				self.tableWidget2.setItem(row, 17, QtWidgets.QTableWidgetItem(str(temp[17])))
				self.tableWidget2.setItem(row, 18, QtWidgets.QTableWidgetItem(str(temp[18])))
				self.tableWidget2.setItem(row, 19, QtWidgets.QTableWidgetItem(str(temp[19])))
				self.tableWidget2.setItem(row, 20, QtWidgets.QTableWidgetItem(str(temp[20])))
				self.tableWidget2.setItem(row, 21, QtWidgets.QTableWidgetItem(str(temp[21])))
				self.tableWidget2.setItem(row, 22, QtWidgets.QTableWidgetItem(str(temp[22])))
				self.tableWidget2.setItem(row, 23, QtWidgets.QTableWidgetItem(str(temp[23])))
				self.tableWidget2.setItem(row, 24, QtWidgets.QTableWidgetItem(str(temp[24])))
				self.tableWidget2.setItem(row, 25, QtWidgets.QTableWidgetItem(str(temp[25])))
				self.tableWidget2.setItem(row, 26, QtWidgets.QTableWidgetItem(str(temp[26])))
				self.tableWidget2.setItem(row, 27, QtWidgets.QTableWidgetItem(str(temp[27])))
				self.tableWidget2.setItem(row, 28, QtWidgets.QTableWidgetItem(str(temp[28])))
				self.tableWidget2.setItem(row, 29, QtWidgets.QTableWidgetItem(str(temp[29])))
				self.tableWidget2.setItem(row, 30, QtWidgets.QTableWidgetItem(str(temp[30])))
				self.tableWidget2.setItem(row, 31, QtWidgets.QTableWidgetItem(str(temp[31])))
				self.tableWidget2.setItem(row, 32, QtWidgets.QTableWidgetItem(str(temp[32])))
				self.tableWidget2.setItem(row, 33, QtWidgets.QTableWidgetItem(str(temp[33])))
				self.tableWidget2.setItem(row, 34, QtWidgets.QTableWidgetItem(str(temp[34])))
				self.tableWidget2.setItem(row, 35, QtWidgets.QTableWidgetItem(str(temp[35])))
				self.tableWidget2.setItem(row, 36, QtWidgets.QTableWidgetItem(str(temp[36])))
				self.tableWidget2.setItem(row, 37, QtWidgets.QTableWidgetItem(str(temp[37])))
				self.tableWidget2.setItem(row, 38, QtWidgets.QTableWidgetItem(str(temp[38])))
				self.tableWidget2.setItem(row, 39, QtWidgets.QTableWidgetItem(str(temp[39])))
				self.tableWidget2.setItem(row, 40, QtWidgets.QTableWidgetItem(str(temp[40])))
				self.tableWidget2.setItem(row, 41, QtWidgets.QTableWidgetItem(str(temp[41])))
				self.tableWidget2.setItem(row, 42, QtWidgets.QTableWidgetItem(str(temp[42])))
				self.tableWidget2.setItem(row, 43, QtWidgets.QTableWidgetItem(str(temp[43])))
				self.tableWidget2.setItem(row, 44, QtWidgets.QTableWidgetItem(str(temp[44])))
				self.tableWidget2.setItem(row, 45, QtWidgets.QTableWidgetItem(str(temp[45])))
				self.tableWidget2.setItem(row, 46, QtWidgets.QTableWidgetItem(str(temp[46])))
				self.tableWidget2.setItem(row, 47, QtWidgets.QTableWidgetItem(str(temp[47])))
				self.tableWidget2.setItem(row, 48, QtWidgets.QTableWidgetItem(str(temp[48])))
				self.tableWidget2.setItem(row, 49, QtWidgets.QTableWidgetItem(str(temp[49])))
				self.tableWidget2.setItem(row, 50, QtWidgets.QTableWidgetItem(str(temp[50])))
				self.tableWidget2.setItem(row, 51, QtWidgets.QTableWidgetItem(str(temp[51])))
				self.tableWidget2.setItem(row, 52, QtWidgets.QTableWidgetItem(str(temp[52])))
				self.tableWidget2.setItem(row, 53, QtWidgets.QTableWidgetItem(str(temp[53])))
				self.tableWidget2.setItem(row, 54, QtWidgets.QTableWidgetItem(str(temp[54])))
				self.tableWidget2.setItem(row, 55, QtWidgets.QTableWidgetItem(str(temp[55])))
				self.tableWidget2.setItem(row, 56, QtWidgets.QTableWidgetItem(str(temp[56])))
				self.tableWidget2.setItem(row, 57, QtWidgets.QTableWidgetItem(str(temp[57])))
				self.tableWidget2.setItem(row, 58, QtWidgets.QTableWidgetItem(str(temp[58])))
				self.tableWidget2.setItem(row, 59, QtWidgets.QTableWidgetItem(str(temp[59])))
				self.tableWidget2.setItem(row, 60, QtWidgets.QTableWidgetItem(str(temp[60])))
				self.tableWidget2.setItem(row, 61, QtWidgets.QTableWidgetItem(str(temp[61])))
				self.tableWidget2.setItem(row, 62, QtWidgets.QTableWidgetItem(str(temp[62])))
				self.tableWidget2.setItem(row, 63, QtWidgets.QTableWidgetItem(str(temp[63])))
				self.tableWidget2.setItem(row, 64, QtWidgets.QTableWidgetItem(str(temp[64])))
				self.tableWidget2.setItem(row, 65, QtWidgets.QTableWidgetItem(str(temp[65])))
				self.tableWidget2.setItem(row, 66, QtWidgets.QTableWidgetItem(str(temp[66])))
				self.tableWidget2.setItem(row, 67, QtWidgets.QTableWidgetItem(str(temp[67])))
				self.tableWidget2.setItem(row, 68, QtWidgets.QTableWidgetItem(str(temp[68])))
				self.tableWidget2.setItem(row, 69, QtWidgets.QTableWidgetItem(str(temp[69])))
				self.tableWidget2.setItem(row, 70, QtWidgets.QTableWidgetItem(str(temp[70])))
				self.tableWidget2.setItem(row, 71, QtWidgets.QTableWidgetItem(str(temp[71])))
				self.tableWidget2.setItem(row, 72, QtWidgets.QTableWidgetItem(str(temp[72])))
				self.tableWidget2.setItem(row, 73, QtWidgets.QTableWidgetItem(str(temp[73])))

	def calculate(self):

		count_ppl = self.input_ppl.text()
		count_ppl = int(count_ppl)
		sum_colls = []
		total_colls = []
		for coll in range(3, self.tableWidget.columnCount()):
			data = []
			for row in range(0, 9):
				if self.tableWidget.item(row, coll) is not None:
					item = self.tableWidget.item(row, coll).text()
					item = float(item)
				else:
					item = 0
				item = item/1000
				data.append(item)
			sum_collumn = sum(data)
			sum_colls.append(sum_collumn)
		for i in sum_colls:
			total = i*count_ppl
			total_colls.append(total)
		coll = 2
		for i in sum_colls:
			temp = i
			coll = coll+1
			self.tableWidget.setItem(9, coll, QtWidgets.QTableWidgetItem(str(temp)))
		coll = 2
		for i in total_colls:
			temp = i
			coll = coll+1
			self.tableWidget.setItem(10, coll, QtWidgets.QTableWidgetItem(str(temp)))
		count_ppl_d = self.input_ppl_d.text()
		count_ppl_d = int(count_ppl_d)
		sum_colls_d = []
		total_colls_d = []
		for coll in range(3, self.tableWidget2.columnCount()):
			data_d = []
			for row in range(0, 3):
				if self.tableWidget2.item(row, coll) is not None:
					item = self.tableWidget2.item(row, coll).text()
					item = float(item)
				else:
					item = 0
				item = item/1000
				data_d.append(item)
			sum_collumn_d = sum(data_d)
			sum_colls_d.append(sum_collumn_d)
		for i in sum_colls_d:
			total = i*count_ppl_d
			total_colls_d.append(total)
		coll = 2
		for i in sum_colls_d:
			temp = i
			coll = coll+1
			self.tableWidget2.setItem(3, coll, QtWidgets.QTableWidgetItem(str(temp)))
		coll = 2
		for i in total_colls_d:
			temp = i
			coll = coll+1
			self.tableWidget2.setItem(4, coll, QtWidgets.QTableWidgetItem(str(temp)))

	def push_to_db(self):
		signal = 3
		date = self.input_date.text()
		item = self.input_ppl.text()
		item_d = self.input_ppl_d.text()
		date_op = (date,)
		item = int(item)
		item_d = int(item_d)
		ppl = (item,)
		ppl_d = (item_d,)
		row = 10
		data = []
		for coll in range(4, self.tableWidget.columnCount()):
			if self.tableWidget.item(row, coll) is not None:
				item = self.tableWidget.item(row, coll).text()
				item = float(item)
			else:
				item = 0
			data.append(item)
			val_ch = tuple(data)

		add_n_to_db(signal, ppl, date_op, val_ch)

		row_d = 4
		data_d = []
		for coll in range(4, self.tableWidget2.columnCount()):
			if self.tableWidget2.item(row_d, coll) is not None:
				item = self.tableWidget2.item(row_d, coll).text()
				item = float(item)
			else:
				item = 0
			data_d.append(item)
			val_ch_d = tuple(data_d)


		add_n_to_db(signal, ppl_d, date_op, val_ch_d)

	def exportToExcel(self):
		timedate = time.ctime()
		ppl = self.input_ppl.text()
		ppl_d = self.input_ppl_d.text()
		timefile = timedate[4:10]
		dinner = ' Обід'
		formatfile = '.xlsx'
		file = ppl+' чол.'+timefile+formatfile
		file_d = ppl_d+' чол.'+timefile+dinner+formatfile
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

		for j in range(self.tableWidget2.model().columnCount()):
			columnHeaders.append(self.tableWidget2.horizontalHeaderItem(j).text())
			df = pd.DataFrame(columns=columnHeaders)
		for row in range(self.tableWidget2.rowCount()):
			for col in range(self.tableWidget2.columnCount()):
				try:
					temp = self.tableWidget2.item(row, col).text()
				except:
					temp = 0
				df.at[row, columnHeaders[col]] = temp
				df.to_excel(file_d)


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.tab1 = QtWidgets.QTabWidget()
		#self.tab1.setTabPosition(QtWidgets.QTabWidget.West)
		#self.tab1.setMovable(True)
		self.setCentralWidget(self.tab1)
		self.tab1.addTab(MainTab(), 'Залишки склад')
		self.tab1.addTab(ProfitTab(), 'Прихід')
		self.tab1.addTab(LossTab(), 'Розхід')
		self.tab1.addTab(Menu(), 'Меню вимога')

		self.tab1.addTab(Rozkladka(), 'Розкладка')


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
	win = MyWindow()
	win.resize(1020, 960)
	win.show()
	sys.exit(app.exec_())

