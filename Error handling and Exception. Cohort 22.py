# EXCEPTION AND ERROR HANDLING IN PYTHON

# syntax error
# input error
# logic error
# type error 
# value error
# key error
# tab error
# attribute error 
# name error
# buffer error
# indentation error



# for zero division error
'''
num = 6 
calc = num / 0
print(calc)
'''


'''try:
    num = 6 
    calc = num / 0
    print(calc)
except ZeroDivisionError:
    print('There is a Zero at the denominator')
'''


# for value error
'''
try:
    num = int(input('Enter a number here: ')) 
    calc = num / 3
    print(calc)
except ValueError:
    print('Wrong input')

'''
# for type error
'''
try:
    num = input('Enter your number: ') 
    calc = 7 / num
    print(calc)
except TypeError:
    print('There is an error in the program')
'''
'''
# for name error
try:
    print(x)
except NameError:
    print('There is an error in the code')
'''
'''
# for index error
try:
    my_list=[2,3,4,6,7]
    print(my_list[10])
except IndexError:
    print('index out of range')
'''
'''
# including the else statement
try:
    my_list=[2,3,4,6,7]
    print(my_list[2])
except IndexError:
    print('index out of range')
else:
    print('The code ran successfully. No error was thrown')
'''

'''
# handling multiple errors 
try:
    num1=5
    num2=int(input('Enter Input: '))
    calc=num1/num2
    print(calc)
except ZeroDivisionError:
    print('There is a Zero division error in my code')
except ValueError:
    print('There is a value error in my code')
else:
    print('The code runs perfectly fine')
'''

# including the finally statement
'''
try:
    my_list=[2,3,4,6,7]
    print(my_list[22])
except IndexError:
    print('index out of range')
else:
    print('The code ran successfully. No error was thrown')
finally:
    print('Proceed to the next line of the code')
'''






# using exception
'''
try:
    num1=5
    num2=int(input('Enter Input: '))
    calc=num1/num2
    print(calc)
except ZeroDivisionError:
    print('There is a Zero division error in my code')
except ValueError:
    print('There is a value error in my code')
except Exception as o:
    print(f'Error above. Please cross-check. This is the error in the code: {o} ')

'''

# AssertionError
age=int(input('Enter your age: '))

assert age >= 18, 'Age must be 18 or older'
#assert 'conditionl statement', ' Outputs only when conditional statement is disobeyed
print('You are eligible')


# Raise error
age=int(input('Enter your age: '))
if age < 18:
    raise Exception('You must be 18 or older')
else:
    print('You are eligible')



