# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      To find if a element is found within a file without iterating through the entire 
#      list but rather by spliting the list in half multiple times until we find the element.
# 4. Algorithmic Efficiency
#      I think it is O(logN) as there is only one loop, and every iteration of the loop cuts 
#      the size of the input by a fraction.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was bug finding and bug fixing. Turning the pseudocode into
#      python was easy, as python was made to be very close to pseudocode. However
#      the pseudocode had extra extrapolations that weren't written directly like
#      declaring found and adding the and i_last != 0 part to the while loop.
#      these bugs took me the longest for sure. calculating the algorithmic 
#      efficiency was also difficult as the examples we went over in class
#      were not as complex as this one.
#      
# 6. How long did it take for you to complete the assignment?
#      2 hours
import json

def search(filename, element):


    #filename = input("what file are you looking in: ")



    with open(f'{filename}', 'r') as file:
        names_text = file.read()                # O(1)


    names_json = json.loads(names_text)         # O(1)

 
    names_list = names_json["array"]            # O(1)

    file.close()

    #element = input("what are you looking for in the file?: ")

    i_first = 0                                 #O(1)
    i_last = len(names_list)                    #O(1)
    found = False                               #O(1)

    while i_first <= i_last and not found and i_last != 0: #O(LOG N)
        i_middle = int((i_first+i_last)/2)      #O(1)

        if names_list[i_middle] < element:      #O(1)
            i_first = i_middle + 1
        elif names_list[i_middle] > element:    #O(1)
            i_last = i_middle - 1
        else:
            found = True

    print(f'your element was inside of your document: {found}') #O(1)


def main():
    search('Lab06.empty.json', 'Empty')
    search('Lab06.trivial.json', 'trivial')
    search('Lab06.trivial.json', 'missing')
    search('Lab06.languages.json', 'C++')
    search('Lab06.languages.json', 'Lisp')
    search('Lab06.countries.json', 'United States of America')
    search('Lab06.countries.json', 'United States')

main()





    
