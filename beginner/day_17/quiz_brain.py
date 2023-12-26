class QuizBrain:

  def __init__(self, questions):
    self.quiz_done = False
    self.questions = questions
    self.num_questions = len(questions)
    self.questions_asked = 0
    self.user_score = 0

  def check_answer(self, correct_answer, user_answer):
    if correct_answer == user_answer:
      self.user_score += 1
      print("That's correct, great job!")
    else:
      print("Sorry that's the wrong answer")

  def questions_done(self):
    return self.questions_asked == self.num_questions:

  def ask_question(self):
    if self.questions_done():
      print(f"All done! Final score is: {self.user_score}/{self.num_questions}")
      return
    else: 
      for round_number in range(self.questions_asked, self.num_questions):
        self.questions_asked += 1
        question = self.questions[round_number] 
        question_text = question.text
        question_answer = question.answer
        user_answer = input(f"Q.{round_number}. {question_text} (True/False)?: ") 
        self.check_answer(question_answer, user_answer)
        print(f"Your score: {self.user_score}/{self.questions_asked}.")

      
