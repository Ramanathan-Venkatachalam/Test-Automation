#UnitTesting - Testing a single function
import pytest

def math_sol(num1,operator,num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('We need a int as a inputs to solve the math')

    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f'Invalid operator and cannot solve the math with {operator}')

    if result < 0:
        print('Number is a negative')
    elif result < 10:
        return 'Small number'
    else:
        return 'Really a large number'

class TestMathSol:
    def test_non_int_input_num1(self):
        #error =None
        #try:
            #math_sol('hi', '+', 2)
        #except Exception as e:
            #error = e
        #assert error is not None

        with pytest.raises(Exception) as exc_info:
            math_sol('hi', '+', 2)
        assert 'inputs to solve the math' in str(exc_info)

    def test_non_int_input_num1(self):
        pass

    def test_addition_with_negative_result(self):
        pass
    def test_addition_with_small_result(self):
        assert math_sol(2, '+', 2) == 'Small number'     
    def test_addition_with_large_result(self):
        assert math_sol(20, '+', 3) == 'Really a large number'

    def test_invalid_operator(self):
        pass