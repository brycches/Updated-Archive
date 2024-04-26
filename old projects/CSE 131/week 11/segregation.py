# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      sort a given array using the given segregation sort method
# 4. What was the hardest part? Be as specific as possible.
#     definitely finding the time to do it while also studying for the final.
# 5. How long did it take for you to complete the assignment?
#      3 hours


def segregate (array, i_begin, i_end):
    if i_begin == i_end:
        return i_begin
    i_pivot = int( (i_begin + i_end)/2)
    i_up = i_begin
    i_down = i_end
    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_down] = array[i_down], array[i_up]
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up

def sort_recursive(array, i_begin, i_end):
    if i_end - i_begin <1 or i_end < 0:
        return
    i_pivot = segregate(array, i_begin, i_end)
    sort_recursive(array, i_begin, i_pivot-1)
    sort_recursive(array, i_pivot+1, i_end)


def main():
    array = []
    sort_recursive(array,0,0)
    print(array)
    array = [99]
    sort_recursive(array,0,0)
    print(array)
    array =[49,59,89]
    sort_recursive(array,0,2)
    print(array)
    array =[89, 59, 49]
    sort_recursive(array,0,2)
    print(array)
    array =[11, 99, 12]
    sort_recursive(array,0,2)
    print(array)
    array =[99, 11, 89]
    sort_recursive(array,0,2)
    print(array)
    array =[11, 12, 31, 89, 31]
    sort_recursive(array,0,4)
    print(array)
    array =[85, 85, 50, 31, 31]
    sort_recursive(array,0,4)
    print(array)
    array =[26, 93, 99, 92, 19]
    sort_recursive(array,0,4)
    print(array)
    array =[31, 31, 49, 19, 49]
    sort_recursive(array,0,4)
    print(array)

main()