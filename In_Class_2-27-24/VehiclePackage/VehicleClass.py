#VehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: we need to add maximum speed to the model.
    Change Order: need a way to  'read' the maximum speed from the model.
    Change Order: Some devs need to use the constructor w/o having to provide max speed
    '''
    #constructor. It's called when we instantiate an object of vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @param type: the kind of vehicle
        @param mex_speed: Maximum speed of the Vehicle, defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42    #This is a weak attempt to 'support' data hiding
        self.max_speed = max_speed
    # an instance method. it operates on an instance of the vehicle class     
    def printType(self):
        print(self.type);
        
    def getSpeed(self): # "a getter"
        return self.max_speed    
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass
#Note the indenting!
