import sys
from PyQt5 import QtCore, QtGui, QtWidgets


first_val = ['one', 'two', 'tree']
second_val = [4356, 454, 87]

header_lables = ['first', 'second']
#rows = [('58678', 43), ('0090000', 2)]

rows = []


class MyTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyTab, self).__init__()
        self.parent = parent
        self.rows = list(zip(first_val, second_val))

        self.pushButton = QtWidgets.QPushButton('Создать TableWidget')

        self.pushButton.clicked.connect(self.func_connect)

        self.tableWidget = QtWidgets.QTableWidget(0, 2)
        self.tableWidget.setHorizontalHeaderLabels(header_lables)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.pushButton)


    def func_connect(self):

        self.tableWidget.setRowCount(len(self.rows))
        for row, items in enumerate(self.rows):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(items[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(items[1])))


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        # + vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.tabWidget = QtWidgets.QTabWidget()
        count = self.tabWidget.count()
        self.nb = QtWidgets.QToolButton(text="Добавить", autoRaise=True)
        self.nb.clicked.connect(self.new_tab)
        self.tabWidget.insertTab(count, QtWidgets.QWidget(), "")
        self.tabWidget.tabBar().setTabButton(
            count, QtWidgets.QTabBar.RightSide, self.nb)

        self.new_tab()

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)

    def new_tab(self):
        index = self.tabWidget.count() - 1
        tabPage = MyTab(self)
        self.tabWidget.insertTab(index, tabPage, f"Tab {index}")
        self.tabWidget.setCurrentIndex(index)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    win = MyWindow()
    win.resize(640, 480)
    win.show()
    sys.exit(app.exec_())