#Main.py
# add an import statement for VehicleClass
from VehiclePackage.VehicleClass import *


if __name__ == "__main__":
    # instantiate an object if type vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor
    myCorvette.printType()      # invoke the method of =the object
    
    #invoke the getter for maximum speed. store the return value in a variable
    # print that to the console
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    #instantiate another vehicle object. I make up name
    myAccord = Vehicle("Car")  # myAccord is an object of type Vehicle
    myAccord.printType()            # 
    maximum_speed = myAccord.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # I want a list of three vehicles: car, boat, spaceship
    # I can pick the names and properties 
    # I want some friendly output to demonstrate what I did

    
    myVehicles =  [Vehicle("Accord", 110),
                  Vehicle ("sailboat", 60),
                  Vehicle("Enterprise", 6.706e+8)]
    
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())