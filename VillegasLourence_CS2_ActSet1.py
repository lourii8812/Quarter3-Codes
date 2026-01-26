student_data1 = {}
main = [] 

x = int(input('Enter 1 to start: '))
if x == 1:
    while True:
        print('Menu:')
        print("[1] Add informant")
        print("[2] Make summary")
        print("[0] Exit program")
        
        try:
            x = int(input('Enter Choice: '))
        except ValueError:
            print("Please enter a number.")
            continue

        if x == 1:
            y = input('Student name: ')
            i = input('Age of student: ')
            z = input('Favorite subject: ')
            
            new_student = {"name": y, "age": i, "favsubj": z}
            main.append(new_student)
            
            print(f"Added:\n Name: {new_student['name']} \n Age: {new_student['age']} \n Favorite subject: {new_student['favsubj']}")
        elif x == 2:
            if len(main) > 0:
                print("Summary:")
                for student in main:
                    print(f"Name: {student['name']} | Age: {student['age']} | Fav Subject: {student['favsubj']}")
            else:
                print("No data to summarize!")
        elif x == 0:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")