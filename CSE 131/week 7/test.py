# this is a sorting program

array1 = [5,1,3,9,2,6,4,7,8]
array2 = [0,0,0,0,0,0,0,0,0]

def sublist_stop_finder(i, which_array):
    sublist_stop = ''
    sublist_start = i
    if which_array == 1:
        while sublist_stop == '':
            # print(f'sublist_stop_finder length array1 {len(array1)}')
            # print(f'sublist_stop_finder sublist start {sublist_start}')
            print(f'sublist start {sublist_start}')
            if sublist_start +1 == len(array1):
                sublist_stop = sublist_start
                # print(f"sublist_stop_finder sublist_start , len(array1) {sublist_start , len(array1)}")
                sublist_start += 1
            elif array1[sublist_start] > array1[sublist_start+1]:
                sublist_stop = sublist_start
                # print(f"sublist_stop_finder (this is the stop) array1[sublist_start] , array1[sublist_start+1] {array1[sublist_start] , array1[sublist_start+1]}")
                sublist_start += 1
            elif array1[sublist_start] <= array1[sublist_start+1]:
                # print(f"sublist_stop_finder (this should continue) array1[sublist_start] , array1[sublist_start+1] {array1[sublist_start] , array1[sublist_start+1]}")
                sublist_start += 1
                
        return sublist_stop
    elif which_array == 2:
        while sublist_stop == '':
            # print(f'sublist_stop_finder length array1 {len(array1)}')
            # print(f'sublist_stop_finder sublist start {sublist_start}')
            print(f'sublist start {sublist_start}')
            if sublist_start +1 == len(array1):
                sublist_stop = sublist_start
                # print(f"sublist_stop_finder sublist_start , len(array1) {sublist_start , len(array1)}")
                sublist_start += 1
            elif array2[sublist_start] > array2[sublist_start+1]:
                sublist_stop = sublist_start
                # print(f"sublist_stop_finder (this is the stop) array1[sublist_start] , array1[sublist_start+1] {array1[sublist_start] , array1[sublist_start+1]}")
                sublist_start += 1
            elif array2[sublist_start] <= array2[sublist_start+1]:
                # print(f"sublist_stop_finder (this should continue) array1[sublist_start] , array1[sublist_start+1] {array1[sublist_start] , array1[sublist_start+1]}")
                sublist_start += 1
                
        return sublist_stop



def array_sorter(sublist1_start, sublist1_end, sublist2_start, sublist2_end, which_array, array_start):
    print(f'{which_array} which_array')
    if which_array == 1:
        print(sublist1_start, sublist2_end)
        for i in range (sublist1_start, sublist2_end+1):
            print(f'i {i}')
            print(f"sublist1_start {sublist1_start} <= sublist1_end {sublist1_end} and ( sublist2_end {sublist2_end} == sublist2_start {sublist2_start} or array1[sublist1_start] {array1[sublist1_start]} < array1[sublist1_end] {array1[sublist1_end]})")
            if (sublist1_start <= sublist1_end and ( sublist2_start == sublist2_end or array1[sublist1_start] < array1[sublist1_end])):
                print(f"sublist1_start {sublist1_start} <= sublist1_end {sublist1_end} or sublist2_start {sublist2_start} == sublist2_end {sublist2_end}")
                print (f'array1[sublist1_start] {array1[sublist1_start]} < array1[sublist2_start] {array1[sublist2_start]} ')
                array2[i] = array1[sublist1_start]
                print(array1)
                print(array2)
                sublist1_start += 1
            else:
                print('else')
                print (f'array1[sublist1_start] {array1[sublist1_start]} > array1[sublist2_start] {array1[sublist2_start]} ')
                array2[i] = array1[sublist2_start]
                print(array1)
                print(array2)
                sublist2_start += 1
    elif which_array == 2:
        for i in range (sublist1_start, sublist2_end+1):
            print(f'i {i}')
            if (sublist1_start <= sublist1_end and ( sublist2_start == sublist2_end or array2[sublist1_start] < array2[sublist1_end])):
                array1[i] = array2[sublist1_start]
                print (f'array1[sublist1_start] {array1[sublist1_start]} < array1[sublist2_start] {array1[sublist2_start]} ')
                print(array1)
                print(array2)
                sublist1_start += 1
            else:
                print('else')
                print (f'array1[sublist1_start] {array1[sublist1_start]} > array1[sublist2_start] {array1[sublist2_start]} ')
                array1[i] = array2[sublist2_start]
                print(array1)
                print(array2)
                sublist2_start += 1








        """
        for i_first_subarray in range (sublist1_start, sublist1_end+1):
            for i_second_subarray in range (sublist2_start, sublist2_end+1):
                print(f'sublist2_start, {sublist2_start}, sublist2_end+1, {sublist2_end+1}, sublist1_start, {sublist1_start}, sublist1_end+1, {sublist1_end+1}, i_first_subarray, {i_first_subarray}, i_second_subarray, {i_second_subarray}')
                print(f"1: array_start {array_start} {array2}")
                print(f"array1[i_first_subaray] {array1[i_first_subarray]}, array1[i_second_subarray] {array1[i_second_subarray]} ")
                if sublist2
                if array1[i_first_subarray] < array1[i_second_subarray]:
                    print(f'1 before array2[array_start], {array2[array_start]}')
                    array2[array_start]= array1[i_first_subarray]
                    print(f'1 after array2[array_start], {array2[array_start]}')
                    array_start += 1
                elif array1[i_first_subarray] > array1[i_second_subarray]:
                    print(f'2 before array2[array_start], {array2[array_start]}')                    
                    array2[array_start]= array1[i_second_subarray]
                    print(f'2 after array2[array_start], {array2[array_start]}')
                    array_start += 1
                elif array1[i_first_subarray] == array1[i_second_subarray]:
                    print(f'3 before array2[array_start], {array2[array_start]}')
                    array2[array_start]= array1[i_second_subarray]
                    print(f'3 after array2[array_start], {array2[array_start]}')
                    array_start += 1
                print(f"6: array_start {array_start}{array2}")
    elif which_array == 2:
        for i_first_subarray in range (sublist1_start, sublist1_end+1):
            for i_second_subarray in range (sublist2_start, sublist2_end+1):
                print(f'sublist2_start,{sublist2_start}, sublist2_end+1,{sublist2_end+1}, sublist1_start,{sublist1_start} sublist1_end+1,{sublist1_end+1} i_first_subarray,{i_first_subarray}, i_second_subarray, {i_second_subarray}')
                print(f"2: array_start {array_start}{array1}")
                if array2[i_first_subarray] < array2[i_second_subarray]:
                    array1[array_start]= array2[i_first_subarray]
                    array_start += 1
                    print('1')
                elif array2[i_first_subarray] > array2[i_second_subarray]:
                    array1[array_start]= array2[i_second_subarray]
                    array_start += 1
                    print('2')
                elif array2[i_first_subarray] == array2[i_second_subarray]:
                    array1[array_start]= array2[i_second_subarray]
                    array_start += 1
                    print('3')
            print(f"5: array_start {array_start}{array1}")
            """

def make_sublists(array_start, which_array):
    done = False
    print(f'array start {array_start}')
    sublist1_start = array_start
    sublist1_end = sublist_stop_finder(array_start, which_array)
    # print(f"sublist 1 start {sublist1_start}")
    # print(f"sublist1_end {sublist1_end}")
    # print(f"length array1 {len(array1)}")
    if sublist1_end +1 == len(array1):
        done = 'again'
    if done == False:
        sublist2_start = sublist1_end + 1
        sublist2_end = sublist_stop_finder(sublist2_start, which_array)
        # print(f"sublist 2 start {sublist2_start}")
        # print(f"sublist2_end {sublist2_end}")
        # print(f"length array1 {len(array1)}")
        return sublist1_start, sublist1_end, sublist2_start, sublist2_end, done
    elif done == 'again':
        return sublist1_start, sublist1_end, 0, 0, 'again'
    elif sublist1_start == 0 and sublist1_end == len(array1):
        return sublist1_start, sublist1_end, 0, len(array1), True

def which_array_finder(which_array):
    # print(f'before which_array = {which_array}')
    if which_array == 1:
        which_array = 2
        return 2
        # print(f'if which_array = {which_array}')
    elif which_array == 2:
        which_array = 1
        return 1
        # print(f'elif which_array = {which_array}')
    else:
        which_array = 1
        print(f'else which_array = {which_array}')
        return 1

    return which_array

def main():
    done = False
    array_start = 0
    which_array = 1
    first_pass = True

    while done == False:
        print(f"before sort array1 {array1}")
        print(f"before sort arrray2 {array2}")
        sublist1_start, sublist1_end, sublist2_start, sublist2_end, done = make_sublists(array_start, which_array)
        print(f"sublist1_start, sublist1_end, sublist2_start, sublist2_end, done {sublist1_start, sublist1_end, sublist2_start, sublist2_end, done}")
        if done == 'again':
            array_start = 0
            which_array = which_array_finder(which_array)
        array_start = sublist1_start
        array_sorter(sublist1_start, sublist1_end, sublist2_start, sublist2_end, which_array, array_start)
        print(f'sublist2_end {sublist2_end}')
        
        if sublist2_end == len(array1) - 1:
            array_start = 0
            which_array = which_array_finder(which_array)
        else:
            print(f'main array start {array_start}')
            array_start = sublist2_end + 1
        print(f"3: array_start {array_start}")
        print(f"after sort array1 {array1}")
        print(f"after sort array2 {array2}")

    print(array1, array2)

if __name__ == "__main__":
    main()
