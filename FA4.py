numstudents = int(input("Enter number of students: "))
numsubjects = int(input("Enter number of subjects: "))

classtotal = 0
student = 1

while student <= numstudents:
    print("Student ", student)
    studenttotal = 0
    subject = 1

    while subject <= numsubjects:
        score = float(input(f"Enter score {subject}: "))
        studenttotal += score
        subject += 1

    studentaverage = studenttotal / numsubjects
    print(f"Average for Student {student} = {studentaverage:.1f}")

    classtotal += studentaverage
    student += 1

classaverage = classtotal / numstudents
print(f"\nClass Average = {classaverage:.1f}")
