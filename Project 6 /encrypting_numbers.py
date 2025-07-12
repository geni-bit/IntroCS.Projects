def swap(my_list):
    """The swap function takes a list of integers,
    and swaps the positions of the numbers in pairs."""

    #Get the length of the list
    length = len(my_list)

    #Iterate through the list in steps of 2 to swap the numbers in pairs
    for index in range(0,length-1,2):
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

    return my_list

def add_to_evens(my_list):
    """The function add to evens takes  list of integers, and for any entry
    that is an even integer, add 2 to it."""

    #Get the length of the list
    length = len(my_list)

    #Iterate through each number in the list
    for index in range(0,length):
        if my_list[index] % 2 == 0:  #Check if the numbers in list is even
           my_list[index] = my_list[index] + 2 #Add 2 to the even number
        else:
            my_list[index] #else if the numbers are odd then they stay name 

    return my_list

def left_circular_shift(my_list):
    """The function left circular shift takes a list of integers,
    and performs a left circular shift. Every entry is shifted one
    position to the left, and the first entry becomes the new last entry."""

    #Get the length of the list
    length = len(my_list)

    #a variable for the first number in the list
    first_number = my_list[0]

    #Using a for loop to shift the numbers in the list to the left
    for index in range(length-1):
        my_list[index] = my_list[index + 1]

    #Making the last number be the first number in the list
    my_list[-1] = first_number
    
    return my_list

def encrypt(my_list):

    #Create a copy of my list
    new_list = my_list

    #Applying the swap function to the new list
    swap(new_list)

    #Applying the add to evens function to the new list
    add_to_evens(new_list)

    #Applying the left circular shift function to the new list
    left_circular_shift(new_list)

    #Applying the swap function again to the new list
    swap(new_list)

    return new_list
