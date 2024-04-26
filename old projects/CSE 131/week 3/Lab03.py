# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      Calculate the way a month looks based off of what January 1753 looks like
# 4. What was the hardest part? Be as specific as possible.
#       This assignment went very well for me, as it both totally shook off all the python cobwebs
#       but was also somthing new and challenging. I had to remember all the things we had learned in
#       CSE 130, as well as CSE 111, and try to be as efficient as possible. I'm not quite
#       sure about my compute_days_month function, as i could have used a for loop instead of
#       all the if statements, but the if statements were easy enough, and if i had more than the
#       12 months that i needed to do it for I definitely would have used a for loop.
# 5. How long did it take for you to complete the assignment?
#      3 hours, roughly, maybe a bit more



def get_input():
    """
    gets both the wanted year and wanted month from the user
    error handles to ensure clean inputs
    """
    while True:
        try:
            wanted_year = int(input("What year is your desired month in (1753-∞): "))
            wanted_month = int(input("What month of the year would you like to be displayed? (1-12): "))
            if wanted_year >= 1753 and wanted_month >= 1 and wanted_month <= 12:
                return wanted_month, wanted_year
            else:
                print("Please enter a valid number within the given ranges. ")
        except:
            print("Please enter a valid number within the given ranges. ")

def compute_leap_year(wanted_month, wanted_year):
    """
    calculates the number of years that are leap years between 1753 and the desired year
    as well as adding one extra if it is past the 2nd month and the current year is a leap year
    """
    assert(type(wanted_month) == type(wanted_year) == type(0))
    assert(1 <= wanted_month <= 12)
    assert(1753 <= wanted_year)
    leap_year_count = 0
    for year in range(1753, wanted_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    leap_year_count += 1
    
    if ((wanted_year % 4 == 0 and wanted_year % 100 != 0) or (wanted_year % 400 == 0)) and wanted_month >2:
         leap_year_count += 1
    return leap_year_count

def compute_days_year(wanted_year):
    assert(type(wanted_year) == type(0))
    assert(1753 <= wanted_year)
    days = 365 * (wanted_year - 1753)
    return days

def compute_days_month(wanted_month):
    assert(type(wanted_month) == type(0))
    assert(1 <= wanted_month <= 12)
    days = 0
    

    if wanted_month >= 2:
         days += 31

    if wanted_month >= 3:
         days += 28

    if wanted_month >= 4:
         days += 31
    
    if wanted_month >= 5:
        days += 30
    
    if wanted_month >= 6:
        days += 31
    
    if wanted_month >= 7:
        days += 30

    if wanted_month >= 8:
         days += 31
    
    if wanted_month >= 9:
         days += 31

    if wanted_month >= 10:
        days += 30
    
    if wanted_month >= 11:
         days += 31

    if wanted_month >= 12:
        days += 30    
        
    assert(0 <= days < 365)

    return days


def compute_offset(wanted_month, wanted_year):
    """
    Computes the offset by taking the modulous 7 of the total number of days.
    Calls the compute_days_month function, compute_days_year function, and 
    compute_leap_year function to calculate the total number of days.
    returns the offset.
    """
    assert(type(wanted_month) == type(wanted_year) == type(0))
    assert(1 <= wanted_month <= 12)
    assert(1753 <= wanted_year)
    assert(0<=compute_days_month(wanted_month)<365)
    offset = (compute_days_month(wanted_month) + compute_days_year(wanted_year) + compute_leap_year(wanted_month, wanted_year))%7

    assert(0<= offset <= 6)
    return offset

def display(wanted_month, wanted_year):
    assert(type(wanted_month) == type(wanted_year) == type(0))
    assert(1 <= wanted_month <= 12)
    assert(1753 <= wanted_year)
    month_days = ["","","","","","","","","","","",""]
    leap_day = ((wanted_year % 4 == 0 and wanted_year % 100 != 0) or (wanted_year % 400 == 0)) and wanted_month == 2
    # print(f"leap_day: {leap_day}")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    if leap_day:
         month_days[1] = 29
    # print(f"month_days{month_days}")
    num_days = month_days[wanted_month-1]

    # print(f"wanted_month {wanted_month}, num_days: {num_days}")

    dow = (compute_offset(wanted_month, wanted_year)) + 1
    if dow == 7:
        dow = 0
    # print(f"dow = {dow}")

    display_table(dow,num_days)

    


def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


# Output
# display_table(3, 31)

def main(wanted_month=0, wanted_year=0):
    """runs the program"""
    if wanted_year == 0:
        wanted_month, wanted_year = get_input()

    display(wanted_month, wanted_year)

def test_cases():
    print("January 1753")
    main( 1, 1753)
    print("February 1753")
    main( 2, 1753)
    print("January 1754")
    main(1, 1754)
    print("February 1756")
    main(2, 1756)
    print("February 1800")
    main(2, 1800)
    print("February 2000")
    main(2, 2000)
    main()
    main()

test_cases()
