from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz_brain = QuizBrain(questions=question_bank)

quiz_brain.ask_question()

