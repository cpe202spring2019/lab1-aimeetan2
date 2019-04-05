# Name: Aimee Tan
# Course: CPE 202, Spring 2019
# Assignment: Lab 1

def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    
    if int_list == None:
        raise ValueError

    elif len(int_list) == 0:
        return None

    max_int = 0
    for num in int_list:
        if num > max_int:
            max_int = num
    return max_int    

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    
    if int_list == None:
        raise ValueError

    elif len(int_list) == 1:
        return int_list
    else:
        return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    
    if int_list == None:
        raise ValueError

    if high >= 1:
        middle = (low + high) // 2
        
        if int_list[middle] == target:
            return middle
        elif int_list[middle] > target:
            return bin_search(target, low, middle - 1, int_list)
        else:
            return bin_search(target, middle + 1, high, int_list)

    else:
        return None

 
