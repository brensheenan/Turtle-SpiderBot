import os     # importing os library so as to communicate with the system
import time   # Sleep is needed so that program does not outrun ESC
time.sleep(1)

# This block situationally decides whether the program is running on a Rasberry Pi
# If not, the program runs with no Pi outputs


try:
    import pigpio #importing GPIO library
except(ModuleNotFoundError):
    print("ALERT: you are not running this program on a Raspberry Pi. Initiating debug mode.")
    print("In this mode, nothing will be output to a Raspberry Pi.\n")
    raspberry = False
else:
    os.system ("sudo pigpiod") #Launching GPIO library
    raspberry = True


# Placeholder until above block works properly:
#import pigpio
#os.system ("sudo pigpiod")
#raspberry = True

ESC = 4  #Connect the ESC in this GPIO pin

if raspberry:
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC, 0) 
                
def calibrate(min_value, max_value):   #This is the auto calibration procedure of a normal ESC
    print("\nBeginning calibration.")
    print("\nFirst, disconnect the battery.")
    input("Press Enter when disconnected:")
    if raspberry: pi.set_servo_pulsewidth(ESC, max_value)
    time.sleep(1)

    print("\nNow, plug in the battery. You will hear a series of beeps.")
    input("Press Enter after 3 beeps:")
    if raspberry: pi.set_servo_pulsewidth(ESC, min_value)
    time.sleep(1)

    print("\nWait for this pattern: 2 short beeps, then 2 long beeps.")
    print("After you hear this pattern, disconnect the battery again.")
    input("Press Enter when disconnected:")
    time.sleep(1)

    print("\nNow, plug the battery back in.")
    print("You should hear 3 short beeps, then a low beep and a high beep.")
    print("If you hear this, then calibration was successful.\n")
    time.sleep(1)

            
def test(min_value, max_value):
    print("\nBeginning testing")
    time.sleep(1)

    speed = min_value
    loop_bool = True
    print("\nControls:")
    print("a - 100 decrease   s - 10 decrease   d - 10 increase   f - 100 increase")
    print("q - quit")
    time.sleep(1)

    print("\nMin speed =", min_value)
    print("Max speed =", max_value)
    
    while loop_bool:
        if raspberry: pi.set_servo_pulsewidth(ESC, speed)
        print("\nspeed = ", speed)
        inp = input("Input command: ")

        # Smooth Speed Control
        n = 10 # Subdivisions for smooth scaling
        
        if inp == "a":
            for i in range(n):
                speed -= 100/n
                time.sleep(1.0/n)
        elif inp == "s":
            speed -= 10
        elif inp == "d":
            speed += 10
        elif inp == "f":    
            for i in range(n):
                speed += 100/n
                time.sleep(1.0/n)
        elif inp == "q":
            speed = min_value
            print("\nspeed = ", speed) 
            loop_bool = False
        else:
            print("Invalid input.")
            
def arm(min_value, max_value): # This is the arming procedure of an ESC (Is it really???)
    print("\nBeginning arming sequence.")
    time.sleep(1)
    input("Connect the battery and press Enter")
    print("Arming...")
    if raspberry: pi.set_servo_pulsewidth(ESC, 0)
    time.sleep(1)
    if raspberry: pi.set_servo_pulsewidth(ESC, max_value)
    time.sleep(1)
    if raspberry: pi.set_servo_pulsewidth(ESC, min_value)
    time.sleep(1)
    print("Arming completed.\n")
    time.sleep(1)

def help():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Calibrate:")
    print("Use when setting up the ESC for the first time. Follow the instructions in the terminal as they appear.")
    print("\nArm:")
    print("Use when starting up an ESC that is already calibrated. Note: unsure if this function is actually necessary, needs further testing.")
    print("\nTest:")
    print("Use to test the ESC and motor. The speed will start at 0, follow the instructions on the terminal to increase and decrease the speed as needed.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
