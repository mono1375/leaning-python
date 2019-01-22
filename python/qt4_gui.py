
import sys
from PyQt4 import QtGui ,QtCore

class window(QtGui.QMainWindow):

    def __init__(self):
        super (window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('MakeQTu_Gui')
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())

run()
