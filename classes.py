class Vehicle:
    #CommonFeaturesORFunctionality  
    model = None
    make = None
    is_engine_on = False
    is_headlight_on = False
    is_driving = False

    def __init__(self,make,model): #MagicMethod Automatically run when you instantiate the object
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'{self.make} {self.model}')

    def turn_on_engine(self): #Methodfunction
        print('Turning engine ON')
        self.is_engine_on = True

    def turn_off_engine(self): #Methodfunction
        print('Turning engine OFF')
        if self.is_driving:
            print('You tried to turn off while driving and crashed!')
            return
        self.is_engine_on = False

    def turn_on_headlight(self):
        print('Turn headlight ON')
        self.is_headlight_on = True

    def turn_off_headlight(self):
        print('Turn headlight OFF')
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print('You cannot drive without turning the engine ON!')
            return
        print('Start Driving')
        self.is_engine_on = True
    
    def stop_driving(self):
        print('Stopping')
        self.is_engine_on = False

class Twowheeler(Vehicle):  #ClassDefinition with Inherited

    def turn_handlebar(self, direction):
        print(f'Turning handlebars {direction}')
    
    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebar('right')
        elif direction == 'right':
            self.turn_handlebar('left')
        else:
            print('Invalid direction')    

class Fourwheeler(Vehicle):  #ClassDefinition wuth Inherited
    
    def turn_steering(self, direction):
        print(f'Turning steering wheel {direction}')
    
    def turn(self, direction):
        if direction in ['right', 'left']:
            self.turn_steering(direction)
        #if direction == 'left':
            #self.turn_steering('left')
        #elif direction == 'right':
            #self.turn_steering('right')

        else:
            print('Invalid direction')    


bike = Twowheeler('HeroHonda', 'Splender') #Instance of the class or object
car = Fourwheeler('Tata', 'Nexon')

for vehicle in [bike, car]:
    print(vehicle)

    vehicle.turn_on_engine()
    vehicle.turn_on_headlight()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    vehicle.turn_off_engine() 
    vehicle.turn_off_headlight()

    print('=============================')