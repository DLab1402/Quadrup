from leg import leg
import numpy as np
class body:
    def __init__(self,L,W,arm1,arm2):
        self.__sh =np.array([[[1,0,0,W/2],
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
                    [0,0,0,1]]])
        self.__arm1 = arm1
        self.__arm2 = arm2

    def forward(self,frame_trans,leg_para):
        cal_leg = leg(self.__arm1,self.__arm2)
        state = np.zeros([4,3,4])
        for idx,sh in enumerate(self.__sh):
            base = np.dot(frame_trans,sh)
            state[idx][0] = np.dot(base,[0,0,0,1])
            cal_leg.forward(leg_para[idx][0],leg_para[idx][1],leg_para[idx][2])
            state[idx][1] = np.dot(base,cal_leg.elbow)
            state[idx][2] = np.dot(base,cal_leg.paw)
        return state
    
# a = body(2,2,1,1)
# frame_trans = np.array([[1,0,0,0],
#                [0,1,0,0],
#                [0,0,1,0],
#                [0,0,0,1]])
# leg_para = np.array([[0,0,0],
#             [0,0,0],
#             [0,0,0],
#             [0,0,0]])
# state = a.forward(frame_trans,leg_para)
# print(state)