# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      to sort an array of numbers in numerical order by subdividing the given array into subarrays that are in numerical order, then comparing those sub-arrays until the subarray is the size of the entire array, which we then retrun as sorted.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-




def sort(array):
    # size= None
    # src = None
    # des = None
    # num = None
    # new_source = None
    # begin1 = None
    # end1 = None
    # begin2 = None
    # end2 = None
    # i = None
    size = len(array); # # print(f"lineC: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    src = array; # # print(f"lineD: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    des = [0] * size; # # print(f"lineE: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    num = 2; # print(f"lineF: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    new_source = src; # print(f"lineG: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    while num >1:
        # print(f"lineH: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        num = 0; # print(f"lineI: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        begin1 = 0; # print(f"lineJ: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        if new_source == src:
            while begin1 < size:
                # print(f"lineK: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                end1 = begin1 +1; # print(f"lineL: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                while end1 < size and src[end1-1] <= src[end1]:
                    # print(f"LineM: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                    end1 += 1; # print(f"LineN: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                begin2 = end1; # print(f"LineO: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                if begin2 < size:
                    end2 = begin2+1; # print(f"LineP: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                else:
                    end2 = begin2; # print(f"LineQ: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                while end2 <size and src[end2 -1] <= src[end2]:
                    # print(f"LineR: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                    end2 += 1; # print(f"LineS: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                num += 1; # print(f"LineT: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                # new_source =combine(src, des, begin1, begin2, end2, array, size, src, des, num, new_source)
                new_source =combine(src, des, begin1, begin2, end2)
                begin1 = end2; # print(f"LineAB: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        if new_source == des:
            while begin1 < size:
                # print(f"LineAC: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                end1 = begin1 +1; # print(f"LineAD: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                while end1 < size and des[end1-1] <= des[end1]:
                    # print(f"LineAE: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                    # print(f"LineAF: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                    end1 += 1; # print(f"LineAG: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                begin2 = end1; # print(f"LineAH: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                if begin2 < size:
                    end2 = begin2+1; # print(f"LineAI: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                else:
                    end2 = begin2; # print(f"LineAJ: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                while end2 <size and des[end2 -1] <= des[end2]:
                    # print(f"LineAK: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                    end2 += 1; # print(f"LineAQ: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                num += 1; # print(f"LineAR: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
                # new_source =combine(des, src, begin1, begin2, end2, array, size, src, des, num, new_source)
                new_source =combine(des, src, begin1, begin2, end2)
                begin1 = end2; # print(f"LineAS: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")

        # print(f"LineAT: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    if new_source == src:
        return src
    else:
        return des

# def combine(source, destination, begin1, begin2, end2, array, size, src, des, num, new_source):
def combine(source, destination, begin1, begin2, end2):
    # i = None
    # end1 = None
    # print(f"LineU: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    # print(f'source {source}, destination {destination}, begin1 {begin1}, begin2 {begin2}, end2 {end2}')
    end1 = begin2; # print(f"LineV: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    for i in range(begin1, end2):
        # print(f"LineW: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        if (begin1 < end1) and ( begin2 == end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]; # print(f"LineX: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
            begin1 += 1; # print(f"LineY: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
        else:
            destination[i] = source[begin2]; # print(f"LineY: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
            begin2 += 1; # print(f"(LineZ: array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    # print(f' done source {source}, destination {destination}, begin1 {begin1}, begin2 {begin2}, end2 {end2}')
    # print(f"LineAA: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    return destination

def main(array):
    # array = None
    # size = None
    # src = None
    # des = None
    # num = None
    # new_source = None
    # begin1 = None
    # end1 = None
    # begin2 = None
    # end2 = None
    # i = None
    # print(f"lineA: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    # array = [3,2,1]; # # print(f"lineB: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")
    sorted_array1 = sort(array)
    print(sorted_array1)
    # print(f"LineAU: (array, {array}) (size, {size}) (src, {src}) (des, {des}) (num, {num}) (new_source, {new_source}) (begin1, {begin1}) (end1, {end1}) (begin2, {begin2}) (end2, {end2}) (i, {i})")




def test_cases():
    main([])
    main([1])
    main([1,2,3])
    main([3,2,1])
    main([1,3,5,7,9,11,13,15,17])
    main([17,15,13,11,9,7,5,3,1])
    main([17,32,5,12,67,3,9,1,8,5,80])
    # main(['this is', 'an array', 'containing strings', 'and', 3])
    main('error')   
test_cases()