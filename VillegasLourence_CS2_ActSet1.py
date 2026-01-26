student = {"name" : "", "age" : "", "favsubj" : ""}
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
            student['name'] = y
            student['age'] = i
            student['favsubj'] = z
            studentd = student.copy()
            main.append(studentd)
            
            print(f"Added:\n Name: {student['name']} \n Age: {student['age']} \n Favorite subject: {student['favsubj']}")
        elif x == 2:
            if len(main) > 0:
                print("Summary:")
                for studentz in main:
                    print(f"Name: {studentz['name']} | Age: {studentz['age']} | Fav Subject: {studentz['favsubj']}")
            else:
                print("No data to summarize!")
        elif x == 0:
            print("Exiting program...")
            break

        else:

            print("Invalid choice! Try again.")
