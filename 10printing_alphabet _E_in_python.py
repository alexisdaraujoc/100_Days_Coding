# Day 10: Printing alphabet 'E' in python

def print_letter_E(rows):
    for row in range(rows):
        for col in range(rows):
            if col == 0 or (row == 0 or row == rows // 2 or row == rows - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()

rows = int(input('Enter number of row for the letter E (minimun 5 rows): '))
print_letter_E(rows)
