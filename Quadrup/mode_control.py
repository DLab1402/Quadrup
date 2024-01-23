
class mode_control:
    def __init__(self,monitor):
        self.mode_list = ['Manual','Trot']
        self.monitor = monitor
    
    def action(self,mode):
        if mode == "Manual":
            self.__manual()

    def __manual(self):
        while self.monitor.mode_state == 1:
            # data = self.monitor.read_data()
            print([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
            self.monitor.update_state([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
