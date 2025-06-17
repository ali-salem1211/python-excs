# Take score input from the user
score = int(input("Enter your score (0-100): "))

# Determine and print the letter grade
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")
