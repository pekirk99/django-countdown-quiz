from django.shortcuts import render

def quiz_view(request):
    # Static questions for quick setup
    questions = [
        {
            "id": 1,
            "text": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Paris", "C": "Madrid", "D": "Rome"},
            "correct_option": "B"
        },
        {
            "id": 2,
            "text": "Which programming language is known as 'Python'?",
            "options": {"A": "Snake", "B": "Java", "C": "Python", "D": "C++"},
            "correct_option": "C"
        },
        {
            "id": 3,
            "text": "What is 5 + 7?",
            "options": {"A": "12", "B": "10", "C": "15", "D": "13"},
            "correct_option": "A"
        },
    ]

    if request.method == "POST":
        score = 0
        for question in questions:
            user_answer = request.POST.get(f"question_{question['id']}")
            if user_answer == question["correct_option"]:
                score += 1
        return render(request, "quiz/result.html", {"score": score, "total": len(questions)})

    return render(request, "quiz/quiz.html", {"questions": questions})
