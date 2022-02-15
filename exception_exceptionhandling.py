def print_sum(num1,num2):
    try:
        print(num1+num2)
    except Exception:
        print('Could not add')

print_sum(1, 'hello')
print_sum(1, 5)

def print_mul(num1,num2):
    if type(num1) != int or type(num2) != int:
        raise Exception("Input is not a ints")
    print(num1*num2)

print_mul(2, 2)
try:
    print_mul(2, 'Mul')
except Exception as e:
    print(f'Something is wrong: {e}')