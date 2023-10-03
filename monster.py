#function definition
def AddTwoYumms(x , y) :
    print(x, "+",  y, "is", x+y)
    
#here's the main section of the code 
AddTwoYumms(4,6)

import random

def monstergen():
    num = random.randrange(0, 100)
    if num < 25:
          print("a skeleton appeared")
    elif num < 70:
              print ("a zombie chases you!")
    elif num < 40:
              print ("a spider attacks!")
    elif num < 45:
              print ("a spider attacks!")
    else:
              print ("nothing spawned!")
              
              
while True: #game loop
       monstergen() #function call 
       choice = input("enter any key to continue...")
