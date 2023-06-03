# Day 5: Linear search in python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# taking input from the user
elements = input('Enter the elements of the list (space separated): ').split()
# converting the string list into the integer 
my_list = [int(a) for a in elements]
# taking input from the user to search for the element 
target = int(input('Enter the element to search for: '))
index = linear_search(my_list, target)
if index != -1:
    print('Element', target, 'found at index', index)
else:
    print('Element', target, 'not found in list.')
