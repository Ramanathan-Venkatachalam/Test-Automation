#if-statements
num1= 10
if num1 == 5:
    print('num1 is 5')
elif num1 == 6:
    print('num1 is 6')
else:
    print('num1 is not 5,6')

#oneline if-statements
print('num1 is 5') if num1 == 5 else print('something else')

#forloop
for number in range(5): #using rangefunction
    print(number)

for letter in ['a','b','c']:
    print(letter.upper()) #uppercase function
