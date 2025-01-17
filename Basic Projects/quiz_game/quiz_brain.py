class QuizBrain:
    def __init__(self, question_number, question_list):
        self.question_number = question_number
        self.question_list = question_list
        self.wrong_answers = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        response = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].text} (True or False)?: ")
        self.check_answer(response, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, response, answer):
        if response == answer:
            print("That's Correct!")
            print(f"The correct answer was: {answer}")
            print(f"Your current score is {self.question_number + 1 - self.wrong_answers}/{self.question_number + 1}.")
            print()
        else:
            self.wrong_answers += 1
            print("That's Wrong!")
            print(f"The correct answer was: {answer}")
            print(f"Your current score is {self.question_number + 1 - self.wrong_answers}/{self.question_number + 1}.")
            print()
