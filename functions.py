#printfunction
print('hello') #single parameter or arguments
print('hi', 'all') #multiple parameter or arguments

#function

#function definition with arguments
def area_of_rectangle(length, breath):    
    #body
    result = length * breath
    return result

#functioncall
print(area_of_rectangle(3, 4))
print(area_of_rectangle(6, 12))

def area_of_rectangle(length, breath=5):    
    #body
    result = length * breath
    return result

#functioncallofoptionalargument
print(area_of_rectangle(3))

#operator
import operator #importing inbuilt operator package from PSL
print(operator.add(2, 2))
print(operator.mul(4, 3))