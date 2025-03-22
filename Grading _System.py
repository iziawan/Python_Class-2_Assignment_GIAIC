def grading_system(marks):
    if marks >= 90:
        return "Grade: A+ | Excellent!"
    elif marks >= 80:
        return "Grade: A | Very Good!"
    elif marks >= 70:
        return "Grade: B | Good Job!"
    elif marks >= 60:
        return "Grade: C | Satisfactory!"
    elif marks >= 50:
        return "Grade: D | Needs Improvement!"
    else:
        return "Grade: F | Failed, Try Again!"

# Taking user input for marks
marks = int(input("Enter your marks: "))

# Checking if marks are within range (0-100)
if 0 <= marks <= 100:
    grade = grading_system(marks)  # Calling function to get the grade
    print(grade)  # Displaying the result
else:
    print("Please enter a number between 0 and 100.")  # Error message for invalid range
