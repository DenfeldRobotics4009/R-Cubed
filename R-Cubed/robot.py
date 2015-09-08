#!/usr/bin/env python3

import wpilib

class RCubed(wpilib.IterativeRobot):

    def robotInit(self):
        """This initialises the robot."""
        
        self.robot_drive = wpilib.RobotDrive(0,1)
        self.stick = wpilib.Joystick(0)
        self.hall = wpilib.DigitalInput(0)
        self.analog_hall = wpilib.AnalogInput(0)
        self.spike = wpilib.Relay(1)
        
    def autonomousInit(self):
        """This gets run once when the robot enters auton."""
        pass
    
    def autonomousPeriodic(self):
        """This gets called periodically during auton."""
        pass
    
    def teleopPeriodic(self):
        """This gets called periodically during teleop."""
        self.robot_drive.arcadeDrive(self.stick)
        if self.stick.getTrigger():
            self.spike.set(self.spike.Value.kForward)
        else:
            self.spike.set(self.spike.Value.kOff)
            
    def disabledPeriodic(self):
        self.robot_drive.arcadeDrive(self.stick)
        print({"Analog Hall": self.analog_hall.get(), "Digital Hall": self.hall.get()})
    
if __name__ == "__main__":
    wpilib.run(RCubed)
