import numpy as np
class leg:
    def __init__(self,l2,l3):
        self.__l2 = l2
        self.__l3 = l3

    def forward(self,alpha,beta,lamda):
        self.elbow = np.dot(self.__T01(alpha), self.__T12(beta,self.__l2))
        self.paw = np.dot(self.elbow,np.array([self.l3*np.cos(lamda),self.__l3*np.sin(lamda),0,1]))
        x = self.paw[0]
        y = self.paw[1]
        z = self.paw[2]
        return x,y,z

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
# a = one_leg(1,1)
# print(a.forward(-3.14/2,0,0))