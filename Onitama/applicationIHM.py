import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        
        
        
        
        
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
