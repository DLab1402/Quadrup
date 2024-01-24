import sys
from mode_control import mode_control
from monitor import Monitor
from qua_ble import qua_speak
from PyQt5.QtWidgets import QApplication

class main_qua():
    __connector = None
    mode_state = 0
    __tem_d_joint = [0,0,0,0,0,0,0,0,0,0,0,0]
    def __init__(self):
        self.__app = QApplication(sys.argv)    
        self.__monitor = Monitor()
        self.__monitor.Connect.clicked.connect(self.Connect_button)
        self.__monitor.Disconnect.clicked.connect(self.Disconnect_button)
        self.__monitor.Run.clicked.connect(self.Run_button)
        self.__monitor.Run.setEnabled(False)
        self.__monitor.Pause.setEnabled(False)
        self.__monitor.Stop.setEnabled(False)
        self.__monitor.Pause.clicked.connect(self.Pause_button)
        self.__monitor.Stop.clicked.connect(self.Stop_button)
        self.__mode = mode_control(self)
    
        self.__monitor.Mode.addItem("Manual")
        for mode in self.__mode.mode_list:
            self.__monitor.Mode.addItem(mode)
        self.__monitor.show() 
        sys.exit(self.__app.exec_())

    #Callback function
    def Connect_button(self):
        self.__connector = qua_speak("b8:d6:1a:be:a4:62")
        isco = self.__connector.connect()
        if isco == 1:
            self.__monitor.BLE_list.addItem("Quadrup")
            self.__monitor.Connect.setEnabled(False)
            self.__monitor.Run.setEnabled(True)
        else:
            self.__monitor.BLE_list.addItem("Fail connect")
            self.__connector = None

    def Disconnect_button(self):
        if self.__connector != None:
            self.__monitor.Connect.setEnabled(True)
            self.__connector = None
            self.__monitor.BLE_list.removeItem(0)
            self.__monitor.Run.setEnabled(False)

    def Run_button(self):
        self.mode_state = 1
        self.__monitor.Run.setEnabled(False)
        self.__monitor.Pause.setEnabled(True)
        self.__monitor.Stop.setEnabled(True)
        self.__mode.action(self.__monitor.Mode.currentText())

    def Pause_button(self):
        self.mode_state = 2

    def Stop_button(self):
        self.mode_state = 0
        self.__monitor.Run.setEnabled(True)
        self.__monitor.Pause.setEnabled(False)
        self.__monitor.Stop.setEnabled(False)

    #Support function
    def read_data(self):
        state = self.__connector.read()
        return state
    
    def send_data(self,data):
        self.__connector.send(data)

    def update_state(self,data):
        for i in range(4):
            for j in range(3):  
                self.__monitor.a_joint[j+i*3].setText(str(data[j+i*3+3]))
        self.__monitor.Roll.setText(str(data[0]))
        self.__monitor.Pitch.setText(str(data[1]))
        self.__monitor.Yaw.setText(str(data[2]))

    def take_d_joint(self):
        joint = []
        for i in range(4):
            for j in range(3):  
                joint.append(self.__monitor.d_joint[j+i*3].value())
        return joint
    
    def show(self):
        self.__monitor.show()
#test script
a = main_qua()