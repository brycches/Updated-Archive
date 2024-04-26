students = {
    "G1": ["Nevile", "Longbottom"],
    "S1": ["Tom", "Riddle"],

}


students = {
    "G1": ["Nevile", "Longbottom"],
    "S1": {
        "first_name":"Tom",
        "last_name": "Riddle",
    } 
}


WAND = 0
FNAME = 1
LNAME = 2

students = {
    "G1": ["Unicorn Cherry Wood", "Nevile", "Longbottom"],
    "S1": ["Elder Wand","Tom", "Riddle"],

}

print( students["S1"][WAND]) == print( students["S1"][0])




WAND = 0
FNAME = 1
LNAME = 2

students = {
    "G1": ["Unicorn Cherry Wood", "Nevile", "Longbottom"],
    "S1": ["Elder Wand","Tom", "Riddle"],

}

for student in students:
    print(student)

looking_for = '123'

if looking_for in students:
    pass

for student_id in students:
    student = students[student_id]
    print(f"{student[FNAME]} {student[LNAME]} uses {student[WAND]}.")


looking_for = 'G2' #  looking_for = input("What is the student ID you are looking for? ")

if looking_for in students:
    print (f"{looking_for} is a student")
else:
    print (f"{looking_for} is not a student!")







