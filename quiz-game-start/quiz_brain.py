class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans,current_question.answer)

    def still_has_questions(self):
        return len(self.questions_list)  > self.question_number

    def check_answer(self, user_ans, answer):
        if user_ans.lower() == answer.lower():
            self.score += 1
            print("You got it!")
        else:
            print("Wrong answer.")

        print(f"Correct answer is: {answer}")  