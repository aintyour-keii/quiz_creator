import os
import random

# Checking if the "quizzes" folder exists:
# If not, create "quizzes" folder
quizzes_folder = "quizzes"
os.makedirs(quizzes_folder, exist_ok=True)

# Create Main Menu:
# Option 1. Create Quiz
# Option 2. Take Quiz
# Option 3. Exit

# Wait for user input
# If input is 1, proceed to create quiz
# If input is 2, proceed to take a quiz
# If input is 3, exit the program
# If something else, print "Invalid input", return to main menu
def main_menu():
    print("\nQuiz Program")
    print("1. Create a Quiz")
    print("2. Take Quiz")
    print("3. Exit")

    user_input = input("Enter an option: ").strip()
    if user_input == "1":
        print("Proceeding to create a quiz.")
        create_quiz()
    elif user_input == "2":
        print("Select a quiz to take.")
        take_quiz()
    elif user_input == "3":
        print("Thank you for using the Quiz Creator Program. Goodbye!")
        quit()
    else:
        print("Invalid input. Please choose 1 or 2 or 3.")
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
    
    with open(file_path, "w", encoding="utf-8") as file:
        # Create *.txt file:
        # Write Title in file
        file.write(f"{quiz_title.title()}\n")

        # For each question:
        for index, question_data in enumerate(questions, start=1):
            # Write question number and text(question itself) in file
            file.write(f"{index}. {question_data['question']}\n")

            # Create choices list by combining answer with other options
            choices = [question_data['answer']] + question_data['other_options']

            # Shuffle all choices (correct + other options)
            letters = ["A", "B", "C", "D"]
            random.shuffle(choices)

            # Write choices as A-D:
            for i, choice in enumerate(choices):
                letter = letters[i]
                # Correct answer ends with "*"
                # Choices are on a new line
                if choice == question_data['answer']:
                    file.write(f"{letter}. {choice}*\n")
                else:
                    file.write(f"{letter}. {choice}\n")
            # Add empty space so that questions are not squished together.
            file.write("\n")

    # Print "Quiz Successfully Created: {file_name}"
    print(f"Quiz Successfully Created: {snake_case_title}.txt")
    # Return to main menu
    main_menu()

# Create "Take Quiz" function
def take_quiz():
    """
    Responsible for quiz selection
    """
    # Store the created quiz files in a list
    quizzes = []
    for file in os.listdir(quizzes_folder):
        if file.endswith(".txt"):
            quizzes.append(file)
    
    # Check if there are created quizzes
    # -> If there are proceed with selecting a quiz to take
    # -> If there are none, return to main menu
    if not quizzes:
        print("No quizzes found. Please create one first.")
        return main_menu()
    
    # Quiz Selection:
    print("Select A Quiz:")
    # Enumarate the quizzes with corresponding numbers as id (1. Quiz Title)
    for id, quiz in enumerate(quizzes, start=1):
        print(f"{id}. {str(quiz).replace(".txt","").replace("_"," ").title()}")
    # Ask for user input to select a quiz
    try:
        choice = int(input("Select a quiz number to take: "))
        # Check if user input is within the range of valid ids for the quizzes
        # If input is valid, proceed with running the quiz
        if 1 <= choice <= len(quizzes):
            quiz_path = os.path.join(quizzes_folder, quizzes[choice - 1])
            run_quiz(quiz_path)
        else: # If input is invalid, call the "Take Quiz" function again.
            print("Invalid number.")
            take_quiz()
    except ValueError:
        print("Please enter a valid number.")
        take_quiz()

# Create "Run Quiz" function with a parameter for the quiz file path
def run_quiz(file_path):
    """
    Responsible for actual taking of the quiz.
    Handles scores, quiz progess, and shows correct answers.
    Randomizes the questions and its corresponding choices.
    """
    # Open the quiz file using the provided path
    with open(file_path, "r", encoding="utf-8") as file:
        # Read all lines from the file and strip whitespaces
        lines = [line.strip() for line in file.readlines()]

    # Display the quiz title (first line of the file)
    print(f"\nStarting Quiz: {lines[0]}\n")

    # Initialize an empty list to store questions
    questions = []
    line_index = 1
    # Start reading from the second line onward
    while line_index < len(lines):
        # If a line starts with a number and dot (e.g., 1.), it's a question
        # Continue until all questions are read
        if lines[line_index] and lines[line_index][0].isdigit() and lines[line_index][1] == ".":
            question_text = lines[line_index]
            line_index += 1
            choices = []
            # Read the next 4 lines as choices
            for _ in range(4):
                letter, choice = lines[line_index].split(". ", 1)
                # Determine which choice has a "*" indicating it's correct
                is_correct = choice.endswith("*")
                # Strip "*" and store each choice with a flag indicating correctness
                if is_correct:
                    choice = choice[:-1]
                choices.append({"text": choice, "is_correct": is_correct})
                line_index +=1

            # Add the question and its choices to the list
            questions.append({
                "question": question_text[question_text.find('.') + 1:].strip(),
                "choices": choices
            })
        else:
            line_index += 1
    
    # Shuffle the questions randomly
    random.shuffle(questions)
    # Initialize score to 0
    score = 0
    # Initialize list to store user results
    user_results = []
    
    # Loop through each question
    for i, question_data in enumerate(questions, start=1):
        # Display the question
        if i == 1:
            print(f"{i}. {question_data['question']}")
        else:
            print(f"\n{i}. {question_data['question']}")

        # Shuffle the choices
        choices = question_data['choices']
        random.shuffle(choices)

        letter_map = {}
        correct_letter = ""
        # Assign letters (A, B, C, D) to each choice
        for i, choice in enumerate(choices):
            letter = chr(65 + i)
            letter_map[letter] = choice
            # Track the correct answer letter
            if choice['is_correct']:
                correct_letter = letter
            print(f"{letter}. {choice['text']}")

            # Ask for user input (A/B/C/D)
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            # Check if the answer is correct and update score
            is_answer_correct = user_answer == correct_letter
            if is_answer_correct:
                score += 1
            # Store the result with user answer and correct answer
            user_results.append({
                "question_num": i,
                "user_letter": user_answer,
                "correct_letter": correct_letter,
                "user_choice": letter_map.get(user_answer, {"text": "Invalid"}).get("text", "Invalid"),
                "correct_choice": letter_map[correct_letter]["text"],
                "is_correct": is_answer_correct
            })

    print("\n=== QUIZ RESULTS ===")
    # After all questions are answered
    # Display quiz results
    for result in user_results:
        # For each question, show if correct or incorrect
        if result["is_correct"]:
            print(f"{result['question_num']}. {result['user_letter']}. {result['user_choice']}")
        else:
            # If incorrect, show the correct answer
            print(f"{result['question_num']}. {result['user_letter']}. {result['user_choice']} -> {result['correct_letter']}. {result['correct_choice']}")

    # Display the total score
    print(f"\nSCORE: {score}/{len(questions)}\n")
    # Return to the main menu
    main_menu()

main_menu()
