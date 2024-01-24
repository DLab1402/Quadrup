from PyQt5.QtCore import QThread

class mode_control(QThread):
    def __init__(self,monitor):
        super().__init__()
        self.mode_list = ['Trot']
        self.monitor = monitor
        self.pre_d_joint = self.monitor.take_d_joint()
    
    def action(self,mode):
        self.mode = mode
        self.start()
        
    def run(self):
        while self.monitor.mode_state == 1:
            if self.mode == "Manual":
                self.__manual()

    def __manual(self):
        data = self.monitor.read_data()
        self.monitor.update_state(data)
        print(self.monitor.take_d_joint())
        cur_d_joint = self.monitor.take_d_joint()
        if self.pre_d_joint == cur_d_joint:
            self.monitor.send_data(cur_d_joint)
        
        self.pre_d_joint = cur_d_joint
        # self.monitor.show()
        self.quit()
