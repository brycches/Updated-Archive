
#i_pivot =''
#i_largest = ''
#i_largest_position = ''
import json

def sort(filename):
    #filename = input ('what is your file named? ')

    with open(f'{filename}', 'r') as file:
        names_text = file.read()                # O(1)


    names_json = json.loads(names_text)         # O(1)

    
    names_list = names_json["array"]            # O(1)

    file.close()

    example = names_list

    assert type(example) == type([])

    #example = [ 26, 6, 90, 55,] # O(1)  ; print(f" a: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")#a 

    i_pivot = len(example) - 1 # O(1); print(f" b: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
    assert type(i_pivot) == type(0)
    assert 0 <= i_pivot < len(example)
    
    while i_pivot >= 0: #O(n)
        largest = example[i_pivot] # O(1); print(f" c: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        i_largest_position = 0 # O(1); print(f" d: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        #print (f"i_largest 1 = {i_largest} example[i_pivot] = {example[i_pivot]} i_pivot = {i_pivot}") 
        for i, i_check in enumerate(example[0:i_pivot]): # O(log 1/n n)
            #print (f"i_largest 2 = {i_largest} icheck 1 = {i_check}")
            if i_check > largest:
                largest = i_check #; print(f" e: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
                #print (f"i_largest 3 = {i_largest} icheck 2 = {i_check}")
                i_largest_position = i #; print(f" f: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        #print (f"i_largest 4 = {i_largest} example[i_pivot] = {example[i_pivot]}i_pivot = {i_pivot}")
        if largest > example[i_pivot]: #j
            example[i_largest_position], example[i_pivot] =  (
                example[i_pivot], example[i_largest_position]) ; # print(f" g: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
            #print (f"i_largest 5 = {i_largest} example[i_pivot] = {example[i_pivot]}i_pivot = {i_pivot}")
        i_pivot = i_pivot - 1 #; print(f" h: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")


    print(f"{example}") #; print(f" i: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
            

def sort2(filename):
    assert type(filename) == str

    with open(f'{filename}', 'r') as file:
        names_text = file.read()                # O(1)


    names_json = json.loads(names_text)         # O(1)


    names_list = names_json["array"]            # O(1)

    file.close()

    example = names_list

    assert type(example) == type([])

    #example = [ 26, 6, 90, 55,] # O(1)  ; print(f" a: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")#a 

    i_pivot = len(example) - 1 # O(1); print(f" b: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
    assert type(i_pivot) == type(0)
    assert 0 <= i_pivot < len(example)


    #while i_pivot >= 0: #O(n)
    for data in example:
        assert 0 <= i_pivot < len(example)
        largest = example[i_pivot] # O(1); print(f" c: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        
        i_largest_position = 0 # O(1); print(f" d: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        #print (f"i_largest 1 = {i_largest} example[i_pivot] = {example[i_pivot]} i_pivot = {i_pivot}") 
        for i, check in enumerate(example[0:i_pivot]): # O(log 1/n n)
            #print (f"i_largest 2 = {i_largest} icheck 1 = {i_check}")
            assert type(check)== type(largest)
            if check > largest:
                largest = check #; print(f" e: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
                #print (f"i_largest 3 = {i_largest} icheck 2 = {i_check}")
                i_largest_position = i #; print(f" f: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
        #print (f"i_largest 4 = {i_largest} example[i_pivot] = {example[i_pivot]}i_pivot = {i_pivot}")
        if largest > example[i_pivot]: #j
            example[i_largest_position], example[i_pivot] =  (
                example[i_pivot], example[i_largest_position]) #;  print(f" g: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")
            #print (f"i_largest 5 = {i_largest} example[i_pivot] = {example[i_pivot]}i_pivot = {i_pivot}")
        i_pivot = i_pivot - 1 #; print(f" h: ipivot {i_pivot} i_largest {i_largest} i_largest_position {i_largest_position} example {example}")

    assert type(example) == type([])
    print(f"{example}")



sort2("file.json")