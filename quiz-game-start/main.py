from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_txt = question['text']
    questions_ans = question['answer']
    new_question = Question(question_txt, questions_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
     quiz.next_question()

print("\nYou completed the quiz!")
print(f"The final score is: {quiz.score} / {quiz.question_number}")