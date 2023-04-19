import RPi.GPIO as GPIO   
import sys       
from time import sleep
def main(argv):
    mode = "f"
    speed = 50
    
    
    
    in1 = 24
    in2 = 23
    en = 25

    en2 = 17
    in3 = 22
    in4 = 27

    temp1=1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p1 =GPIO.PWM(en2,1000)

    p.start(25)
    p1.start(25)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")    

    while(1):

        x=mode
        
        p.ChangeDutyCycle(float(speed))
        p1.ChangeDutyCycle(float(speed))
    


        if x=='s':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            temp1=1
            x='z'

        elif x=='b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            temp1=0
            x='z'

        elif x=='s':
            print("low")
            p.ChangeDutyCycle(speed)
            p1.ChangeDutyCycle(speed)
            
        elif x=='r':
            print("right")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x = 'z'
        elif x=='l':
            print("right")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            x = 'z'
        
        
        elif x=='e':
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
            
            
if __name__ == "__main__":
   main(sys.argv[1:])