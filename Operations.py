# Elizabeth Fuller
# 2/10/2020
# List operators methods. uses 5 numbers in a list

import collections

def sort_list(list):
    return sorted(list)


def sum_of_list(list):
    # adds the numbers in the list together
    total = 0
    for num in list:
        total = total + num
    return total


def product(list):
    # multiplies the numbers in the list together
    total = 1
    for num in list:
        total = total * num
    return total


def mean(list):
    # finds the average of the list
    i = 1
    total = 0
    for num in list:
        total = total + num
        i = i + 1
    average = total/i
    return average


def median(list):
    # finds the median of a list of 5 numbers
    sort = sorted(list)
    medi = sort[2]
    return medi


def modes(numbers):
    # finds the mode of the list of numbers
    data = collections.Counter(numbers)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(numbers):
        return "No mode"
    else:
        return mode_val


def largest(list):
    # find the largest number
    lar = 0
    for num in list:
        if num > lar:
            lar = num
    return lar


def smallest(list):
    # find the smallest number
    small = list[0]
    for num in list:
        if num < small:
            small = num
    return small


def no_dups(list):
    # creates a new list without duplicates
    list3 = sorted(list)
    list4 = []
    [list4.append(x) for x in list3 if x not in list4]
    return list4


def no_even(list):
    # creates new list without evens
    list_odd = []
    for num in list:
        if num % 2 != 0:
            list_odd.append(num)

    return list_odd


def no_odd(list):
    # creates new list without odds
    list_eve = []
    for num in list:
        if num % 2 == 0:
            list_eve.append(num)

    return list_eve
    return


def look_for(list, search):
    # look for a number in the list
    for num in list:
        if search == num:
            return True
        else:
            return False
    return


def second_largest(list):
    # find the second largest number
    sort = sorted(list)
    return sort[-2]
