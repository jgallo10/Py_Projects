from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    each_quest = Question(quest["text"],quest["answer"])
    question_bank.append(each_quest)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")