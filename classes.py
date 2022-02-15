class Motorcycle:  #ClassDefinition
    model = None
    make = None
    is_engine_on = False
    is_headlight_on = False

    def __init__(self,make,model): #MagicMethod Automatically run when you instantiate the object
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'{self.make} and {self.model}')

    def turn_on_engine(self): #Methodfunction
        self.is_engine_on = True
        
    def turn_handlebar(self):
        pass
    
bike = Motorcycle('HeroHonda', 'Splender') #Instance of the class or object
print(bike)
print(bike.is_engine_on)
print(bike.is_headlight_on)

bike.turn_on_engine() #methodcall
print(bike.is_engine_on)