from PyQt5 import QtCore, QtWidgets
import sys


class MainWindow(QtWidgets.QWidget): # главное окно
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.tab_bar = QtWidgets.QTabWidget()
        self.tab_bar.addTab(MyTab(MyTable), 'Zalyshky')
        self.tab_bar.addTab(MyTab('Two'), '2')

        #self.label = QtWidgets.QLabel('Hello world')
        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtWidgets.QPushButton('&Close')

        self.vbox = QtWidgets.QVBoxLayout()

        self.vbox.addWidget(self.tab_bar)
        #self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)

        self.setLayout(self.vbox)

        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


class MyTab(QtWidgets.QWidget):
    def __init__(self, text):
        super(MyTab, self).__init__()
        label = QtWidgets.QLabel(f'<center>{text}</center>')
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)


class MyTable(QtWidgets.QWidget):
    def __init__(self, text):
        super(MyTable, self).__init__()
        label = QtWidgets.QTableWidget(3,3)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Title")
    window.resize(1200, 900)
    window.show()
    sys.exit(app.exec_())
