#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()

    if idx < 0:
        return my_list
    elif idx > (length - 1):
        return my_list
    else:
        new_list_1 = new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list