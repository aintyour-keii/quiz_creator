import os

# Checking if the "quizzes" folder exists:
# If not, create "quizzes" folder
quizzes_folder = "quizzes"
os.makedirs(quizzes_folder, exist_ok=True)

# Create Main Menu:
# Option 1. Create Quiz
# Option 2. Exit

# Wait for user input
# If input is 1, proceed to create quiz
# If input is 2, exit the program
# If something else, print "Invalid input", return to main menu
def main_menu():
    print("\nQuiz Creator")
    print("1. Create a Quiz")
    print("2. Exit")

    user_input = input("Enter an option: ").strip()
    if user_input == "1":
        print("Proceeding to create a quiz.")
    elif user_input == "2":
        print("Thank you for using the Quiz Creator Program. Goodbye!")
        quit()
    else:
        print("Invalid input. Please choose 1 or 2.")
        main_menu()

main_menu()

# Create "Create Quiz" function
# Ask for the quiz title: 
# -> if input is "exit", return to main menu
# -> otherwise title to snake_case store to variable
# Loop:
# -> Ask for question input:
# -> Question input format:
#   -> add " ?" at the end if there's none
# -> Ask for correct answer input
# -> Ask for 3 other options
# -> Store the question, correct answer, other options in list
# -> Ask for another question input - y/n; y - continue loop; n - save quiz
# (Outside of loop) Creating a *.txt file in the "quizzes" folder - file name is snake_case title
# Create *.txt file:
# Write Title in file
# For each question:
# -> Write question number and text(question itself) in file
# -> Shuffle all choices (correct + other options):
# -> Write choices as A-D:
#   -> Correct answer ends with "*"
#   -> Choices are on a new line
# -> Add empty space so that questions are not squished together.
# Print "Quiz Successfully Created: {file_name}"
# Return to main menu