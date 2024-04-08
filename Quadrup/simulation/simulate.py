import numpy as np
from body import body
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class simu_body:
    def __init__(self,body_para,time):
        self.time = time
        self.__body = body(body_para[0],body_para[1],body_para[2],body_para[3])
        self.fig = plt.figure()
        self.main_sketch = self.fig.add_subplot(111, projection='3d')
        self.main_sketch.set_xlim([-10,10])
        self.main_sketch.set_xlim([-10,10])
        self.main_sketch.set_xlim([-10,10])
        self.main_sketch.plot([10,-10,-10,10,10],[10,10,-10,-10,10],[-10,-10,-10,-10,-10])


    def animation(self,path,leg_para):
        self.__path = path
        self.__leg_para = leg_para
        self.ani = FuncAnimation(self.fig, self.__sketch, frames=len(path), interval=self.time)
        self.ani.save('animation.gif', writer='pillow')
        plt.show()
    
    def __sketch(self,i):
        self.main_sketch.clear()
        self.main_sketch.plot([10,-10,-10,10,10],[10,10,-10,-10,10],[-10,-10,-10,-10,-10])
        state = self.__body.forward(self.__path[i],self.__leg_para[i])
        shoulders = [state[0][0],state[1][0],state[2][0],state[3][0]]
        self.__body_sketch(shoulders)
        for i in range(4):
            legs = [state[i][0],state[i][1],state[i][2]]
            self.__leg_sketch(legs)

    def __body_sketch(self,shoulders):#shoulders = [4x3]
        x = [shoulders[0][0],shoulders[1][0],shoulders[2][0],shoulders[3][0],shoulders[0][0]]
        y = [shoulders[0][1],shoulders[1][1],shoulders[2][1],shoulders[3][1],shoulders[0][1]]
        z = [shoulders[0][2],shoulders[1][2],shoulders[2][2],shoulders[3][2],shoulders[0][2]]
        self.main_sketch.plot(x, y, z, color='b')
    
    def __leg_sketch(self,leg):
        x = [leg[0][0],leg[1][0],leg[2][0]]
        y = [leg[0][1],leg[1][1],leg[2][1]]
        z = [leg[0][2],leg[1][2],leg[2][2]]
        self.main_sketch.plot(x, y, z, color='b')

a = simu_body([2,2,0.5,0.5],100)
# frame_trans = np.array([[[1,0,0,0],
#                [0,1,0,0],
#                [0,0,1,0],
#                [0,0,0,1]],
#                [[1,0,0,0],
#                [0,1,0,0],
#                [0,0,1,0],
#                [0,0,0,1]]])
# leg_para = np.array([[[-3.14/2,-3.14/4,3.14/2],
#             [-3.14/2,-3.14/4,3.14/2],
#             [-3.14/2,-3.14/4,3.14/2],
#             [-3.14/2,-3.14/4,3.14/2]],
#             [[0,0,0],
#             [0,0,0],
#             [0,0,0],
#             [0,0,0]]])
# a.animation(frame_trans,leg_para)
#Trot walk
frame_trans = []
leg_para = []
for i in range(100):
    frame_trans.append([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]])
    leg_para.append([[-3.14/2,-3.14*np.cos(0.1*i)/4,-3.14*np.cos(0.1*i)/8+3.14/8],
            [-3.14/2,3.14*np.cos(0.1*i)/4,3.14*np.cos(0.1*i)/8+3.14/8],
            [-3.14/2,-3.14*np.cos(0.1*i)/4,-3.14*np.cos(0.1*i)/8+3.14/8],
            [-3.14/2,3.14*np.cos(0.1*i)/4,3.14*np.cos(0.1*i)/8+3.14/8]])
a.animation(frame_trans,leg_para)