from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(0, question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was {quiz.question_number - quiz.wrong_answers}/{quiz.question_number}")