# Elizabeth Fuller
# 2/10/2020
# list operators interface. inputs and outputs

import Operations

lists = []
print("Please enter a series of five values. Use numerals only.")
first = input("First number: ")
first = int(first)
lists.append(first)
second = input("Second number: ")
second = int(second)
lists.append(second)
third = input("Third number: ")
third = int(third)
lists.append(third)
fourth = input("Fourth number: ")
fourth = int(fourth)
lists.append(fourth)
fifth = input("Fifth number: ")
fifth = int(fifth)
lists.append(fifth)

print("This is your list sorted smallest to largest:")
print(Operations.sort_list(lists))

print("This is the sum of your list:")
print(Operations.sum_of_list(lists))

print("This is the product of your list:")
print(Operations.product(lists))

print('This is the average of your list:')
print(Operations.mean(lists))

print("This is the median of your list:")
print(Operations.median(lists))

print("This is the mode of your list:")
print(Operations.modes(lists))

print("This is the largest number in your list:")
print(Operations.largest(lists))

print("This is the second largest number in the list:")
print(Operations.second_largest(lists))

print("This is the smallest number in your list:")
print(Operations.smallest(lists))

print("This is your list without duplicates:")
print(Operations.no_dups(lists))

print("This is your list without even numbers:")
print(Operations.no_even(lists))

print("This is your list without odd numbers:")
print(Operations.no_odd(lists))

print("Enter a number to see if it is in your list: ")
looking = input()
looking = int(looking)
found = Operations.look_for(lists, looking)
if found == True:
    print(f"{looking} is in your list.")
else:
    print(f"{looking} is not in your list.")
