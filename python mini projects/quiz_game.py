'''
Build a 10-question MCQ quiz. Questions stored as list of dicts.
Score at the end. Use functions throughout.
'''

def get_quiz_questions():
    return [
        {
            "question" : "Which planet is known as the Red Planet?",
            "options" : ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Orca"],
            "answer": "B"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Gold", "B) Silver", "C) Oxygen", "D) Hydrogen"],
            "answer": "C"
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "answer": "C"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
            "answer": "C"
        },
        {
            "question": "Which year did World War II end?",
            "options": ["A) 1918", "B) 1939", "C) 1945", "D) 1950"],
            "answer": "C"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
            "answer": "C"
        },
        {
            "question": "What is the main gas found in the air we breathe?",
            "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Argon"],
            "answer": "B"
        },
        {
            "question": "Which programming language is known for its readability and simplicity?",
            "options": ["A) C++", "B) Java", "C) Python", "D) Ruby"],
            "answer": "C"
        }
    ]

def ask_question(question_dict, question_number):
    print(f"Question {question_number} : {question_dict["question"]}")
    for option in question_dict["options"]:
        print(option)

    while True:
        user_choice = input("Choose the options (A, B, C or D)").strip().upper()
        if user_choice in ['A', 'B', 'C', 'D']:
            return user_choice
        else:
            print("Please choose from the ['A', 'B', 'C', 'D'] options only")

def run_quiz():
    print("==== Welcome to the Quiz! ====")
    questions = get_quiz_questions()
    score = 0
    for index, q in enumerate(questions, start=1):
        user_answer = ask_question(q, index)
        if user_answer == q['answer']:
            print("it is correct✨")
            score += 1
        else:
            print(f"oh! it is wrong ❌. The correct answer is {q['answer']}")
    display_results(score, len(questions))

def display_results(score, total_questions):
    print("="*40)
    print(f"Your score is {score}/{total_questions}")


run_quiz()