'''The model for how a question can be made.'''

class Question:
    '''The question class'''
    def __init__(self, q_text, a_text):
        self.question = q_text
        self.answer = a_text
        