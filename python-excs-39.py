questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A) 30", "B) 11", "C) 56", "D) 25"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Dickens", "B) Shakespeare", "C) Tolstoy", "D) Homer"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    if user_ans == q["answer"]:
        score += 1

print(f"\nYou got {score} out of {len(questions)} correct.")
