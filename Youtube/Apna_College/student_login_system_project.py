
#!Login Code
students=[]

def login():
    username="kanji"
    password="Lpe@2025"

    while True:
        u=input("Enter Username Here: ")
        p=input("Enter Password Here: ")

        if u == username and p == password:
            print("Login Sucessfully\n")
            return True
        else:
            if u!=username:
                print("Invalid Username,Try Again!\n")
            else:
                print("Invalid Password,Try Again!\n")

# login()

#!Grade Calculate
"""""
>= 90  → A
>= 75  → B
>= 60  → C
>= 40  → D
< 40   → F"""
def calculate_marks(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks!"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

# c1 = calculate_marks(40)
# print(c1)


#!Add Student

def add_student():
    roll = int(input("Enter Roll No: "))

    for s in students:
        if s["roll"]==roll:
            print("Roll Number Allready Exists!\n")
            return
    name = input("Enter Your Name: ").strip().title()
    marks=int(input("Enter Your Marks Here: "))

    grade=calculate_marks(marks)

    student = {
        "roll":roll,
        "name":name,
        "marks":marks,
        "grade":grade
    }

    students.append(student)
    print("Student Added Sucessfully\n")

#!Display:-

def display_student():
    if not students:
        print("No Student Found!\n")
        return
    for s in students:
        print("Roll",s['roll'])
        print("Name",s["name"])
        print("Marks",s["marks"])
        print("Grade",s["grade"])
        print("-" * 20)
    print()

#!Search

def search_student():
    roll=int(input("Enter Roll No To Search: "))

    for s in students:
        if s["roll"]==roll:
            print(s)
            print()
            return
    print("Student Not Found\n")


#!Update:-

def update_student():
    roll=int(input("Enter Roll No To Update: "))

    for s in students:
        if s['roll']==roll:
            s["name"]=input("Enter New Name: ").strip().title()
            s["marks"]=int(input("Enter New Marks: "))
            s["grade"]=calculate_marks(s["marks"])
            print("Student Updated\n")
            return
    print("Student Not Found\n")

#!Delete Student:-

def del_student():
    roll = int(input("Enter Roll No To Delete: "))

    for s in students:
        if s['roll']==roll:
            students.remove(s)
            print("Student Deleted\n")
            return
    print("Student Not Found\n")

#!Menu:-

def menu():
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Logout")
        print("7. Exit")

        choice=input("Input Choice Here: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            del_student()
        elif choice == '6':
            print("Log Out\n")
            break
        elif choice == '7':
            print("Thank you!")
            exit()
        else:
            print("Invalid Choice\n")
        
#!Main:-

if login():
    menu()
            
    
