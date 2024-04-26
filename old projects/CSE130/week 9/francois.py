# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      Find the nth number in a list of numbers where n = (n-1) + (n-2)
# 4. What was the hardest part? Be as specific as possible.
#      There wasn't very much code to do or to mess up, although while
#      basing my code on the solution provided for the previous week
#      I didn't see the point of the while loop until I saw the do
#      at the top of your pseudocode, which solved the bug/problem.
# 5. How long did it take for you to complete the assignment?
#      3 hours

def francois():
    n = 0
    while n <= 0:
        try:
            n = int(input("What number in this sequence would you like? "))
            if n <= 0:
                print(f"your number must be a positive intiger")
        except:
            print(f"your number must be a whole number")
    assert type(n) == type(0)
    assert n > 0
    array = [1,2]
    if n > 2:
        for index in range (3,n+1):
            assert array[index % 2] == array[1] or array[index % 2] == array[0]
            array[index % 2] = array[0] + array[1]
    value = array[n % 2]
    print (f"the francois number {n} is {value}")


def main():
    francois()
    francois()
    francois()
    francois()
    francois()
main()