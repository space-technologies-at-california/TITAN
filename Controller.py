import numpy as np
import math
import time, threading

#time interval between position measurements
WAIT_SECONDS = 0.01
    

class Controller:
    
    """ Attributes:
        Dict stores time stamps that map to pos data- {time: getData()}
        Constructor takes 3 item acceleration tuple as argument 
        (ax, ay, az) and 3 item gyroscope tuple (rz, ry, rz) to account
        for linear and rotational motion in calculating relative position 
        during trajectory"""
    def __init__(self, accel, gyro):
        self.ax, self.ay, self.az = accel
        self.rx, self.ry, self.rz = gyro
        #initialize position to 0,0,0 at the beginning of each trajectory
        self.sx, self.sy, self.sz = 0,0,0
        self.pitch, self.roll = 0,0
        self.timeData = {}
        self.update()
        

    """ Returns position with error using current accelerometer and 
        gyroscopic data"""
    def calculatePosition(self):
        return 0
    
    """Calculate roll and pitch at each time stamp"""
    def accelRollPitch(self):
        self.pitch = 180 * math.atan(self.ax/math.sqrt(self.ay**2 + self.az**2))/math.pi
        self.roll = 180 * math.atan(self.ay/math.sqrt(self.az**2 + self.ax**2))/math.pi
        return {"Pitch": self.pitch, "Roll": self.roll}

    """ Uses gyroscope and acceleration data to recalculate pitch and roll using 
        complementary filter"""
    def sensorFusion():
        return 0
    
    """"""
    def update(self):
        threading.Timer(WAIT_SECONDS, self.calculatePosition()).start()
        self.timeData[time.time()] = self.getData()

    def getData(self):
        data = {"Position": (self.sx,self.sy,self.sz), "Error": 0, 
                "Acceleration" : (self.ax,self.ay,self.az), 
                "Gyroscope": (self.rz,self.ry,self.rz),
                "Pitch" : self.pitch, "Roll": self.roll}
        return data

    """ Need to record error measurement with each pos measurement"""
