import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QColor

class Monitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.d_joint = []
        for i in range(4):
            for j in range(3):
                self.d_joint.append(QtWidgets.QSlider(self))
                self.d_joint[j+i*3].setMinimum(-45)
                self.d_joint[j+i*3].setMaximum(45)
                self.d_joint[j+i*3].setGeometry(12+147*i,54+96*j,135,30)
                self.d_joint[j+i*3].setOrientation(Qt.Horizontal)



#test script
app = QApplication(sys.argv)
a = Monitor()

if __name__ == '__main__':
    
    a.show()
    sys.exit(app.exec_())