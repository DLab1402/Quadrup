from leg import leg
import numpy as np
class body:
    def __init__(self,L,W,arm1,arm2):
        self.__sh =[[[1,0,0,W/2],
                    [0,1,0,L/2],
                    [0,0,1,0],
                    [0,0,0,1]],
                    [[-1,0,0,-W/2],
                    [0,1,0,L/2],
                    [0,0,1,0],
                    [0,0,0,1]],
                    [[-1,0,0,-W/2],
                    [0,1,0,-L/2],
                    [0,0,1,0],
                    [0,0,0,1]],
                    [[1,0,0,W/2],
                    [0,1,0,-L/2],
                    [0,0,1,0],
                    [0,0,0,1]]]
        self.__arm1 = arm1
        self.__arm2 = arm2

    def forward(self,frame_trans,leg_para):
        cal_leg = leg(self.__arm1,self.__arm2)
        state = np.zeros([4,3])
        for idx,sh in enumerate(self.__sh):
            state[idx][0] = np.dot(frame_trans,sh)
            cal_leg.forward(leg_para[idx][0],leg_para[idx][1],leg_para[idx][3])
            state[idx][1] = np.dot(state[idx][0],cal_leg.elbow)
            state[idx][2] = np.dot(state[idx][0],cal_leg.paw)
        return state