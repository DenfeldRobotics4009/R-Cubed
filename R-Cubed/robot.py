#!/usr/bin/env pyhton3

import wpilib

class RCubed(wpilib.IterativeRobot):

    def robotInit(self):
        """This initialises the robot."""
        
        self.robot_drive = wpilib.RobotDrive(0,1)
        self.stick = wpilib.Joystick(0)
        self.hall = wpilib.DigitalInput(0)
        self.analog_hall = wpilib.AnalogInput(0)
        
    def autonomousInit(self):
        """This gets run once when the robot enters auton."""
        pass
    
    def autonomousPeriodic(self):
        """This gets called periodically during auton."""
        pass
    
    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.stick)
        print({"Analog Hall": self.analog_hall.get(), "Digital Hall": self.hall.get()})
    
if __name == "__main__":
    wpilib.run(RCubed)
