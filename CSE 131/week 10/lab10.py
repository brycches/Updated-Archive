import json
def get_array():
    file_name = input("what is your file's name? ")
    with open(file_name, "r",) as file:
        array = json.load(file)
    return array

array = get_array()
def main():
    array = get_array()
    sorted_array = sorter(array)
    display_array(sorted_array)

def display_array(sorted_array):
	print(sorted_array)

def sorter(array, i_up=0,i_down = len(array)-1, i_pivot = len(array) //2 ):
	if len(array) > 1:
		done = False
		while done == False:
			up_done = False
			down_done = False
			if array[i_up] < array[i_pivot] and i_up < i_pivot:
				i_up += 1
			if array[i_down] > array[i_pivot] and i_down > i_pivot:
				i_down -= 1
			if array[i_up] > array[i_pivot]:
				up_done = True
			if array[i_down] < array[i_pivot]:
				down_done = True
			if i_down == i_pivot and i_up == i_pivot:
				done = True
			if up_done == True and down_done == True and not done:
				if i_up == i_pivot:
					i_pivot = i_down
				elif i_down == i_pivot:
					i_pivot = i_up
				array[i_up], array[i_down] = array[i_down], array[i_up]
			if done == True:
				sorter(array, 0, i_up-1, (i_up-1) // 2)
				sorter(array, i_pivot, len(array)-1, ((len(array)-1) + i_pivot) // 2)
	
		
		
		
def main():
    sorted_array = sorter(array)
    display_array(sorted_array)				
				
				
main()


