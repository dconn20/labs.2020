# A Program that reads in students
# until the user enters a blank
# and then prints them all out again

students = []

firstname = input("Enter first name (blank to quit): ").strip()
while firstname != "":
    student = {}
    student ["firstname"] = firstname
    lastname = input ("Enter lastname: ").strip()
    student ["lastname"] = lastname
    students.append(student)

    firstname = input("Enter first name (blank to quit): ").strip()

print ("Here are the student you entered:")
for currentstudent in students:
    print ("{} {}".format(currentstudent["firstname"], currentstudent ["lastname"])) 
