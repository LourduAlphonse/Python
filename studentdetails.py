students = {}

while True:
    print('Students Record Menu:')
    print('1. Add Student')
    print('2. Remove Student')
    print('3. Update Student')
    print('4. Display Student Details')
    print('5. Search Student')
    choice = input('Enter your choice:')

    if choice == '1':
        student_id = input('Enter student ID: ')
        name = input('Enter student name: ')
        gpa = float(input('Enter student GPA: '))
        students[student_id] = {'name': name,'gpa': gpa}
        print('Student added successfully.')

    elif choice == '2':
        student_id = input('Enter student ID to remove: ')
        if student_id in students:
            del students[student_id]
            print('Student removed successfully.')
        else:
            print('Student not found.')

    elif choice == '3':
        student_id = input('Enter student ID to update: ')
        if student_id in students:
            name = input('Enter new student name: ')
            gpa = float(input('Enter new student GPA: '))
            students[student_id]['name'] = name
            students[student_id]['gpa'] = gpa
            print('Student updated successfully.')
        else:
            print('Student not found')

    elif choice == '4':
        if not students:
            print('No Student in Records.')
        else:
            for student_id, student in students.items():
                print(f'Student Name: {student['name']}')
                print(f'Student ID: {student_id}')
                print(f'Student GPA: {student['gpa']}')

    elif choice == '5':
        name = input('Enter student name to search: ')
        for student_id, student in students.items():
            if student['name'].lower() == name.lower():
                print(f'Student Name: {student['name']}')
                print(f'Student ID: {student_id}')
                print(f'Student GPA: {student['gpa']}')
                break
        else:
            print('Student not found!')

    elif choice == '6':
        print('Thank you for using our student records system!')
        break
    else:
        print('Invalid choice. Please try again.')
