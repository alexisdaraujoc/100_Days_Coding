# Day 6: Check for two consecutive ones

def count_consecutive_ones(lst):
    count = 0
    total = 0
    for num in lst:
        if num == 1:
            count += 1
            if count == 2:
                total += 1
        else:
            count = 0
    return total
elements = input('Enter the elements of the list (space-separated): ').split()
my_list = [int(elem) for elem in elements]

ocurrences = count_consecutive_ones(my_list)
print('Ocurrences of two consecutive ones:', ocurrences)
