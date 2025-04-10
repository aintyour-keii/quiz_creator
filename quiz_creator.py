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
        create_quiz()
    elif user_input == "2":
        print("Thank you for using the Quiz Creator Program. Goodbye!")
        quit()
    else:
        print("Invalid input. Please choose 1 or 2.")
        main_menu()

# Create "Create Quiz" function
def create_quiz():
    # Ask for the quiz title:
    quiz_title = input("Enter quiz title: ").strip()
    # if input is "exit", return to main menu
    if quiz_title.lower() == "exit":
        return main_menu()
    # otherwise convert title to snake_case store to variable
    else:
        snake_case_title = quiz_title.replace(" ", "_").lower()
        print(snake_case_title)

    # Create a quesions list - storage for the questions
    questions = []
    # Loop:
    while True:
        # Ask for question input:
        question = input("Enter question: ").strip()
        # Question input format: add " ?" at the end if there's none
        if not question.endswith("?"):
            question += " ?"

        #  Ask for correct answer input
        answer = input("Enter answer: ").strip()
        # Ask for 3 other options
        other_options = [input("Enter incorrect answer: ").strip() for i in range(3)]

        # Store the question, correct answer, other options in list -> questions storage
        questions.append({
            "question": question,
            "answer": answer,
            "other_options": other_options
        })

        # Ask for another question input - y/n; y - continue loop; n - save quiz
        another_question = input("Would you like to enter another question? (y/n): ").strip().lower()
        if another_question != "y":
            break
    # (Outside of loop) Creating a *.txt file in the "quizzes" folder - file name is snake_case title
    file_path = os.path.join(quizzes_folder, f"{snake_case_title}.txt")
    file = open(file_path, "w", encoding="utf-8")
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

main_menu()
