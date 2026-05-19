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
print("3. Search students")
print("4. Delete Student")
print("5. Exit")

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


    elif choice == "3":
        search_student = input("Enter student name to search :")

        flag = False
        for student in students:
            if search_student == student["name"]:
                 
                print("Student found successfully!")
                print("Name :" , student["name"])
                print("Marks : " , student["marks"])
                flag = True
        
        if flag == False:
             print("Student not found !")

    
    elif choice == "4":
        delete_student = input("Enter student to delete :")
        
        for student in students:
            if delete_student == student["name"]:
                students.remove(student)
                print("student deleted successfully!")

    else:
        print("Exit....")
        break
