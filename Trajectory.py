class Trajectory:
    
    #dictionary variables

    def __init__(self):
        self.numTimeStamps = 0
        self.state = {}

    def getData():
        return 0

    def updateState():
        numTimeStamps+=1
        state.update(numTimeStamps, getData())

    def obstacleDetector():
        return 0
    
    def calculateTrajectory():
        return 0


    #function to return servo rotation angle (from +90 to -90 deg.) given a particular horizontal angle (0 to 359 deg.) and vertical angle (0 to 90 deg) to launch
    def caluclateServos(horDegrees, vertDegrees):
        servo1 = 0
        servo2 = 0
        servo3 = 0

        #If the angle to jump aligns w/ one of the 3 feet angles
        if (horDegrees = 0):
            servo1 = 90 - vertDegrees
            servo2 = -90
            servo3 = -90
        if (horDegrees = 120):
            servo1 = -90
            servo2 = 90 - vertDegrees
            servo3 = -90
        if (horDegrees = 240):
            servo1 = -90
            servo2 = -90
            servo3 = 90 - vertDegrees
        

        return servo1, servo2, servo3
   