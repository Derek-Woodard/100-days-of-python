'''The brain that tracks all information relevant ot the quiz.'''
class QuizBrain:
    '''Each new quiz has a brain that tracks the score and current question.'''
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        '''Asks the next question to the user - Checks the answer.'''
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].question} (True/False): ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        '''Determines if the user has completed all teh questions.'''
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, question_answer):
        '''Checks to see if the user answer was correct.'''
        if user_answer.lower() == question_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
