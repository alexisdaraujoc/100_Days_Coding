# Day 8: Printing special character pattern part 2

def print_special_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + my_input * i)

my_input = input('Enter the special character: ')

num_rows = int(input('Enter the number of rows: '))
print_special_pattern(num_rows)