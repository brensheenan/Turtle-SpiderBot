# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?

from ESC_functions import calibrate, arm, test, help

min_value = 1000  #change this if your ESC's min value is different
max_value = 2000 #change this if your ESC's max value is different

print("Welcome to the ESC test program.")
print("1 - Calibrate")
print("2 - Arm")
print("3 - Test")
print("4 - Help")
print("q - Quit")

loop_bool = True
while loop_bool:
    inp = input("To select a function, enter the corresponding number:")
    if inp == "1":
        calibrate(min_value, max_value)
    elif inp == "2":
        arm(min_value, max_value)
    elif inp == "3":
        test(min_value, max_value)
    elif inp == "4":
        help()
        pass # To do: create help function
    elif inp == "q":
        print("Goodbye")
        loop_bool = False
    else :
        print("Invalid input.")