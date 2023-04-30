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

        DEFAULTPOS = #INSERT Calculation to find default based on leg size

        #If the angle to jump aligns w/ one of the 3 feet
        # 1) Knocks down the rover onto the feet angle
        # 2) Raises the rover to the vertDegrees
        if (horDegrees = 0):
            knockDownRover(1)
            servo1 = 90 - vertDegrees
            servo2 = DEFAULTPOS
            servo3 = DEFAULTPOS
            return servo1, servo2, servo3
        if (horDegrees = 120):
            knockDownRover(2)
            servo1 = DEFAULTPOS
            servo2 = 90 - vertDegrees
            servo3 = DEFAULTPOS
            return servo1, servo2, servo3
        if (horDegrees = 240):
            knockDownRover(3)
            servo1 = DEFAULTPOS
            servo2 = -DEFAULTPOS
            servo3 = 90 - vertDegrees
            return servo1, servo2, servo3


        #If the angle does not align w/ one of the 3 feet
        if(horDegrees < 60 or horDegrees > 300):

        if(horDegrees > 60 and horDegrees < 180):
            
        if(horDegrees > 180 and horDegrees < 300):
            



        return servo1, servo2, servo3

    #A function which knocks down to rover to align with one of the 3 axes corresponding to a leg
    def knockDownRover(servo):

   