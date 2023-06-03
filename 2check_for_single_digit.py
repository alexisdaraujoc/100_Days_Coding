# Day 2: Check for single digit

def get_single_digit(number):
    if len(number) == 1 and number.isdigit(): 
        return True
    else:
        return False

while True:
    input_number = input('enter a number: ')
    if get_single_digit(input_number):
        print('Valid single digit')
        break
    else: 
        print('not a valid single digit. Try again.')

print('Single digit you enter is: ', input_number)

