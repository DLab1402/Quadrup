import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
class leg:
    def __init__(self,l2,l3):
        self.__l2 = l2
        self.__l3 = l3

    def forward(self,alpha,beta,lamda):
        base = np.dot(self.__T01(alpha), self.__T12(beta,self.__l2))
        self.elbow = np.dot(base, [0,0,0,1])
        self.paw = np.dot(base,np.array([self.__l3*np.cos(lamda),self.__l3*np.sin(lamda),0,1]))
        x = self.paw[0]
        y = self.paw[1]
        z = self.paw[2]
        return x,y,z
    
    def invert(self,x,y,z):
        if x**2+y**2+z**2<=(self.__l2+self.__l3)**2:
            tem = (x**2+y**2+z**2-self.__l2**2-self.__l3**2)/(2*self.__l2*self.__l3)
            a = self.__l2+self.__l3*tem
            lamda = np.arccos(tem)
            b = self.__l3*np.sin(lamda)
            if a*b >= 0:
                angle = np.arccos(a/np.sqrt(a**2+b**2))
            else:
                angle = -np.arccos(a/np.sqrt(a**2+b**2))
            
            beta = np.arcsin(y/np.sqrt(a**2+b**2)) - angle
            
            alpha = np.arcsin(z/(self.__l2*np.cos(beta)+self.__l3*np.cos(beta+lamda)))
            return alpha,beta,lamda
        else:
            return 0,0,0

    def animation(self,path,time):
        fig = plt.figure()
        main_sketch = fig.add_subplot(111, projection='3d')
        main_sketch.set_xlim([-10,10])
        main_sketch.set_xlim([-10,10])
        main_sketch.set_xlim([-10,10])
        main_sketch.plot([10,-10,-10,10,10],[10,10,-10,-10,10],[-10,-10,-10,-10,-10])
        def sketch(i):
            main_sketch.clear()
            main_sketch.plot([10,-10,-10,10,10],[10,10,-10,-10,10],[-10,-10,-10,-10,-10])
            alpha,beta,lamda = self.invert(path[i][0],path[i][1],path[i][2])
            x,y,z = self.forward(alpha,beta,lamda)
            main_sketch.plot([0,self.elbow[0]],[0,self.elbow[1]],[0,self.elbow[2]],color='b')
            main_sketch.plot([self.elbow[0],x],[self.elbow[1],y],[self.elbow[2],z],color='b')  
        # for i in range(len(path)):
        #     sketch(i)
        ani = FuncAnimation(fig, sketch, frames=len(path), interval=time)
        ani.save('animation.gif', writer='pillow')
        plt.show()

    def __T01(self,alpha):
        T = np.zeros([4,4])
        T[0][0] = np.cos(alpha)
        T[0][2] = -1*np.sin(alpha)
        T[1][1] = 1
        T[2][0] = np.sin(alpha)
        T[2][2] = np.cos(alpha)
        T[3][3] = 1
        return T
    
    def __T12(self,beta,l2):
        T = np.zeros([4,4])
        T[0][0] = np.cos(beta)
        T[0][1] = -1*np.sin(beta)
        T[0][3] = l2*np.cos(beta)
        T[1][0] = np.sin(beta)
        T[1][1] = np.cos(beta)
        T[1][3] = l2*np.sin(beta)
        T[3][3] = 1
        return T

    
#Test script
a = leg(1,1)
print(a.forward(-3.14/2,0,0))
print(a.invert(1,np.sqrt(3),0))
path = np.zeros([100,3])
for i in range(100):
    path[i][0] = 1+0.5*np.cos(2*3.14/100*i)
    path[i][1] = 0.5*np.sin(2*3.14/100*i)
    path[i][2] = -1
a.animation(path,100)