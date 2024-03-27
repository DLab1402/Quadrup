import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class Monitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,300)
        self.d_joint = []
        self.a_joint = []
        self.d_joint_label = []
        for i in range(4):
            for j in range(3):  
                self.d_joint.append(QtWidgets.QSlider(self))
                self.d_joint[j+i*3].setMinimum(-45)
                self.d_joint[j+i*3].setMaximum(45)
                self.d_joint[j+i*3].setGeometry(12+147*i,54+50*j,135,20)
                self.d_joint[j+i*3].setOrientation(Qt.Horizontal)

                self.a_joint.append(QtWidgets.QLabel(self))
                self.a_joint[j+i*3].setGeometry(107+147*i,30+50*j,40,20)
                self.a_joint[j+i*3].setText('0')
                self.a_joint[j+i*3].setAlignment(Qt.AlignRight)

                self.d_joint_label.append(QtWidgets.QLabel(self))
                self.d_joint_label[j+i*3].setGeometry(67+147*i,30+50*j,40,20)
                self.d_joint_label[j+i*3].setText(str(self.d_joint[j+i*3].value()))
                self.d_joint_label[j+i*3].setAlignment(Qt.AlignRight)

                leg_label = QtWidgets.QLabel(self)
                leg_label.setGeometry(12+147*i,30+50*j,50,20)
                leg_label.setText("leg_"+str(i+1)+"."+str(j))
        
        #Connection control
        self.BLE_list = QtWidgets.QComboBox(self)
        self.BLE_list.setGeometry(12,190,100,20)

        # self.Scan = QtWidgets.QPushButton(self)
        # self.Scan.setGeometry(124,190,50,20)
        # self.Scan.setText("Scan")

        self.Connect = QtWidgets.QPushButton(self)
        self.Connect.setGeometry(186,190,100,20)
        self.Connect.setText("Connect")

        self.Disconnect = QtWidgets.QPushButton(self)
        self.Disconnect.setGeometry(298,190,100,20)
        self.Disconnect.setText("Disconnect")

        #Mode control
        self.Mode = QtWidgets.QComboBox(self)
        self.Mode.setGeometry(12,220,100,20)

        self.Run = QtWidgets.QPushButton("Run",self)
        self.Run.setGeometry(124,220,80,20)

        self.Pause = QtWidgets.QPushButton("Pause",self)
        self.Pause.setGeometry(221,220,80,20)

        self.Stop = QtWidgets.QPushButton("Stop",self)
        self.Stop.setGeometry(318,220,80,20)

        #Roll-Pitch-Yaw monitor
        Roll_lable = QtWidgets.QLabel(self)
        Roll_lable.setText("Roll:")
        Roll_lable.setGeometry(450,190,80,20)

        self.Roll = QtWidgets.QLabel(self)
        self.Roll.setText("0")
        self.Roll.setGeometry(508,190,80,20)
        self.Roll.setAlignment(Qt.AlignRight)

        Pitch_lable = QtWidgets.QLabel(self)
        Pitch_lable.setText("Pitch:")
        Pitch_lable.setGeometry(450,220,80,20)

        self.Pitch = QtWidgets.QLabel(self)
        self.Pitch.setText("0")
        self.Pitch.setGeometry(508,220,80,20)
        self.Pitch.setAlignment(Qt.AlignRight)

        Yaw_lable = QtWidgets.QLabel(self)
        Yaw_lable.setText("Yaw:")
        Yaw_lable.setGeometry(450,252,80,20)

        self.Yaw = QtWidgets.QLabel(self)
        self.Yaw.setText("0")
        self.Yaw.setGeometry(508,252,80,20)
        self.Yaw.setAlignment(Qt.AlignRight)
        

#test script
# app = QApplication(sys.argv)
# a = Monitor()

# if __name__ == '__main__':
    
#     a.show()
#     sys.exit(app.exec_())