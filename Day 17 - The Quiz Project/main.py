'''A program that gives the user a quiz and tracks their score.'''

from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# create the question bank using the question model and the data
question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
