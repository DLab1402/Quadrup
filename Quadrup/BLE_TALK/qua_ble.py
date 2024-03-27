#!/home/tony/bluezenv/bin/python3.11		
import struct		
from bluepy.btle import UUID, Peripheral		
		
class qua_speak(Peripheral):		
    _ctrlUUID=UUID("a15b89c6-1042-4c05-af06-52bb41e51c1e")		
    _dataUUID=UUID("a15b89c6-1042-4c05-af06-52bb41e51c1e")		
		
    def __init__(self, addr):		
        Peripheral.__init__(self,addr)

    def connect(self):
        try: 
            self.discoverServices()		
            self.ctrl_SRV=self.getServiceByUUID(self._ctrlUUID)		
            self.data_SRV=self.getServiceByUUID(self._dataUUID)		
            self.__data = self.data_SRV.getCharacteristics()[0]		
            self.ctrl = self.ctrl_SRV.getCharacteristics()[0]
            return 1		
        except Exception as e:
            print(e)
            return 0

    def __convert_to_bytes(self,number):		
        byte_array = []		
        for n in number:	
            byte_array.extend((n+90).to_bytes(2,byteorder = 'little'))		
        return byte_array

    def __invert_to_real(self,state):
        result = []
        if (len(state) == 38)&(state[0]==state[37]):
            for i in range(15):
                if i<3:
                    result.append(struct.unpack('<f',bytes([state[4*i+1],state[4*i+2],state[4*i+3],state[4*i+4]]))[0])
                if i>=3:
                    tem = [state[2*i+7],state[2*i+8]]
                    result.append(struct.unpack('<H',bytes(tem))[0])
                    
        return result
	
    def send(self,angle):
        angle01 = [12]
        angle01.extend(angle[0:6])
        angle01.extend([12])
        angle02 = [24]
        angle02.extend(angle[6:12])
        angle02.extend([24])
        print(angle01)
        self.__data.write(bytes(self.__convert_to_bytes(angle01)))
        self.__data.write(bytes(self.__convert_to_bytes(angle02)))

    def read(self):
        result = self.__invert_to_real(self.__data.read())
        return result


if __name__ == "__main__":		
    import time		
    cHM10 = qua_speak("b8:d6:1a:be:a4:62")
    ISCo = cHM10.connect()
    print(ISCo)
    angle1 = [1,2,3,4,5,6,7,8,9,10,11,12]		
    # angle2 = [100,30,30,30,30,30,30]		
		
    while True:		
        # tem = cHM10.read()		
        # print(tem)		
        # cHM10.send(angle1)				
        # time.sleep(3.0)		
        cHM10.send(angle1)			
        time.sleep(3.0)		