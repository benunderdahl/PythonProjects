from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)
# new commit

while quiz.still_has_questions():
    quiz.next_question()
    print(f"current score: {quiz.score}/{quiz.number}")

else:
    print("\nThank you for playing")