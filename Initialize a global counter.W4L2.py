# Initialize a global counter

registration_counter = 50000

def student_registration():
    global registration_counter  # Use the global counter
    
    # Generate the Registration ID using the current counter value

    registration_id = registration_counter
    registration_counter += 1   # Increment the counter for the next registration
      
    #this part for user
      
    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_name = input("Enter the Student Name: ")
    student_id = input("Enter the Student ID: ")
    course_name = input("Enter the Course Name: ")
    
    # Display the information
    print("\nthe Student Registration Information are: ")
    print(f"Date: {date}")
    print(f"Student Name: {student_name}")
    print(f"Student ID: {student_id}")

    print(f"Course Name: {course_name}")
    print(f"Registration ID: {registration_id}")

# call the funcation:
student_registration()