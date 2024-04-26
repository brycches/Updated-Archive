# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      create a program that alphabetizes an array of items imported from a json file
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was definitely bug fixing, as "copying" the pseudocode provided 
#      as directly as i knew how did not run correctly. I added many print statements and
#      asserts to check to see if my code did what I thought and to print out the values of the
#      variables at different points in the code to see if they were storing exactly what i
#      assumed, and found after many run throughs that my range functions were the culprit.
#      but i fixed them, and now the code runs phenominally
#      
# 5. How long did it take for you to complete the assignment?
#      4 hours


import json
import time

array = []

def sort(filename):
    #filename = input ('what is your file named? ')
    # Opening the file.
    with open(f'{filename}', 'r') as file:
        names_text = file.read()                
        assert file != ''
        # Loading the file into an array.
        names_json = json.loads(names_text)         

    
        names_list = names_json["array"]            
        # Closing the file.
        file.close()
    # Storing the array into a variable named array.
    array = names_list

    assert type(array) == type([])
    

    # this for loop counts down from the top of the list
    for i_pivot in range(len(array)-1,0,-1):
        assert type(i_pivot) == type(0)
        i_largest = 0
        assert type(i_largest) == type(0)
        # This loop checks all numbers in the array with index values less than 
        # the current index in the first array to see if they are bigger than the
        # item at the current index in the first array.
        for i_check in range(0,i_pivot+1,):
            assert type(i_check) == type(0)
            assert type(array[i_check])== type(array[i_largest])
            
            if array[i_check] > array[i_largest]:
                i_largest = i_check
                assert i_largest == i_check
                assert type(i_largest) == type(0)
                assert type(i_check) == type(0)
        
        
        assert (array[i_largest] >= array[i_pivot])
        # this statement switches the locations of the found biggest value and the item
        # in the index we are looking at, but only if it is bigger, not equal to.
        if array[i_largest] > array[i_pivot]:

            assert array[i_largest] > array[i_pivot]
            array[i_largest], array[i_pivot] =  array[i_pivot], array[i_largest]
            assert (array[i_pivot] >= array[i_largest])

    

    
    assert type(array) == type([])

    # Adding formatting for the print statement so it prints with each item in the 
    # array on its own line and indented
    print(f"{filename} sorted array: [")
    for item in array:
        print(f"    {item}")
    print("]")



# Automation to call my function with the different names of the differnt files
def main():
    sort("Lab08.empty.json")
    # Adding pauses between the differnt files so the example video isn't just me 
    # scrolling through the results of my program.
    time.sleep(2.5)
    sort("Lab08.trivial.json")
    # Adding pauses between the differnt files so the example video isn't just me 
    # scrolling through the results of my program.
    time.sleep(2.5)
    sort("Lab08.languages.json")
    # Adding pauses between the differnt files so the example video isn't just me 
    # scrolling through the results of my program.
    time.sleep(2.5)
    sort("Lab08.states.json")
    # Adding pauses between the differnt files so the example video isn't just me 
    # scrolling through the results of my program.
    time.sleep(2.5)
    sort("Lab08.cities.json")




main()