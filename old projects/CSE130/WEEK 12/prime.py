# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      find all the prime numbers from 1 to the a given maximum, including the maximum.
# 4. What was the hardest part? Be as specific as possible.
#      The test cases. in order to run the test cases in a short video i needed to make the code
#      able to be ran in a function, which broke my code. it wasn't until i figured out why it
#      broke my code that i could fix it, and i found that if i seperated my array into a different
#      function than the one that searched the array, the items i had appended to the array 
#      wouldn't save, even though i was pretty sure arrays usually crossed between functions.
#      I then just made it all into one function and it worked great.
# 5. How long did it take for you to complete the assignment?
#      5 hours


import math
array = []

# def user_array_maker():
#     while True:
#         try:
#             n = int(input("what is your max value?"))
#         except:
#             print("please enter a valid number")

#         if n <= 0:
#             print("please enter a number greater than 0")
#         else:  
#             array = []
#             for numbers in range (1, n+1):
#                 array.append(numbers)
#             print (array)
#             return array
# def array_maker
def prime_finder(n):
    done = False
    while done == False:
        try:
            n = int(n)
        except:
            print("your number is not a valid integer")
            return

        if n <= 0:
            print("prime numbers are greater than 0, please enter a number greater than 0")
            return
        else:  
            array = []
            # This for loop makes an array of all the numbers from 1 to n.
            for numbers in range (1, n+1):
                array.append(numbers)
                assert type(array[0]) == type(0)
                done = True
            
    #def prime_finder():
    for prime_checks in range (2,int(math.sqrt(len(array)))+1):
        # This for loop goes through all the possible roots from 2 to the square root of n
        assert type(prime_checks) == type(0)
        for numbers in range(0,n+1,prime_checks):
            assert type(numbers) == type(0)
            # This loop finds all the numbers that are divisable, and thus not prime, removing them from the array and replacing them with 0
            if   numbers != prime_checks and numbers>0:
                array[numbers-1] = 0 
    primes_array = []
    # This loop looks for all nonzero numbers left in the array, and adds them to thier own unique array.
    for primes in array:
        assert type(primes) == type(0)
        if primes != 0:
            primes_array.append(primes)
    # We then print that unique array that only contains the prime numbers.
    print(primes_array)

# The main function, that calls the other function with all of the test cases hard coded in.
def main():
    print("test case -1:")
    prime_finder(-1)
    print("test case 0:")
    prime_finder(0)
    print("test case 1:")
    prime_finder(1)
    print("test case 2:")
    prime_finder(2)
    print("test case 10:")
    prime_finder(10)
    print("test case 53:")
    prime_finder(53)
    print("test case 100:")
    prime_finder(100)
    print("test case 200:")
    prime_finder(200)


main()