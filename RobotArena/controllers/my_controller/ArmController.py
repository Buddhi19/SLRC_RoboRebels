from controller import Robot

class armcontroll:
    def __init__(self,robot:Robot):
        self.robot=robot
        self.TIME_STEP=32

        #arm components
        self.waist_motor = robot.getMotor('waist_motor')
        self.shoulder_motor = robot.getMotor('shoulder_motor')
        self.elbow_motor = robot.getMotor('elbow_motor')
        self.wrist_motor = robot.getMotor('wrist_motor')
        self.pitch_motor = robot.getMotor('pitch_motor')
       


    def waistcontrol(self,waist_val):
        self.waist_motor.setPosition(waist_val)
        self.waist_motor.setVelocity(0.5)
        self.robot.step(30*self.TIME_STEP)

    def shouldercontrol(self,shoulder_val):
        self.shoulder_motor.setPosition(shoulder_val)
        self.shoulder_motor.setVelocity(0.1)
        self.robot.step(500*self.TIME_STEP)

    def elbowcontrol(self,elbow_val):
        self.elbow_motor.setPosition(elbow_val)
        self.elbow_motor.setVelocity(0.5)
        self.robot.step(40*self.TIME_STEP)

    def wristcontrol(self,wrist_val):
        self.wrist_motor.setPosition(wrist_val)
        self.wrist_motor.setVelocity(0.5)
        self.robot.step(30*self.TIME_STEP)
    
    def pitchcontrol(self,pitch_val):
        self.pitch_motor.setPosition(pitch_val)
        self.pitch_motor.setVelocity(0.5)
        self.robot.step(30*self.TIME_STEP)


    def collectbox(self,waist_val,shoulder_val,elbow_val,wrist_val,pitch_val):
        self.pitchcontrol(pitch_val)
        self.waistcontrol(waist_val)
        self.elbowcontrol(elbow_val)
        self.shouldercontrol(shoulder_val)
        self.wristcontrol(wrist_val)



    def putinback(self,waist_val,shoulder_val,elbow_val,wrist_val,pitch_val):
        self.pitchcontrol(pitch_val)
        self.waistcontrol(waist_val)
        self.elbowcontrol(elbow_val)
        self.shouldercontrol(shoulder_val)
        self.wristcontrol(wrist_val)
        
        
        

