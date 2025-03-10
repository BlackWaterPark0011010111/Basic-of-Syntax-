def start_quiz():
    questions = [
        {"question": "What is Python?", "answer": "A programming language."},
        {"question": "What is a function?", "answer": "A block of code that runs when called."},
        {"question": "What is a loop?", "answer": "A way to repeat actions in a program."},
        {"question": "What is a variable?", "answer": "A place to store data."}
    ]

    score = 0

    for question in questions:
        print(question["question"])
        user_answer = input("YOUR ANSWER: ")

        if user_answer.lower() == question["answer"]. lower():
            print("CORRECT")
            score +=1
        else:
            print(f"INCORRECT. THE CORRECT ANSWER IS: {question['answer']}")
    print(f"YOUR FINAL SCORE IS: {score} / {len(questions)}")
    