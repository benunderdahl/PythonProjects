from itertools import combinations_with_replacement


class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        question = self.q_list[self.number]
        self.number += 1
        user_answer = input(f"\n{question.text} (True/False) ")
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.number < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("correct")
        else:
            print("incorrect")

