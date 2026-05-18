# students = []

# for i in range(3):

#   name = input("Enter Student name : ")
#   students.append(name)
# print(students)


students = []

#for i in range(3):
#    name = input("Enter student name :")
#    marks = int(input("Enter student marks :"))
#
 #   student = {
#        "name" : name,
#        "marks" : marks
 #   }
#
#    students.append(student)
#print(students)


students = []

print("/n Welcome to Student Management System");
print("1.Add Students")
print("2. View Students")
print("3. Exit")

while(True):
    choice = input("Enter choice : ")

    if choice == "1":
        
            name = input("Enter Student name :")
            marks = int(input("Enter student marks : "))

            student = {
                "name" : name,
                "marks" : marks
            }
            students.append(student)
            print("Student Added Successfully!")

    elif choice == "2":
        print(students)

    else:
        print("Exit....")
        break
