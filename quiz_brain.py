class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no}: {question.text} (True/False)? ")

        self.check_ans(ans, question.ans)

    def check_ans(self, user_ans, ans):
        if ans == user_ans:
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
            print(f"The correct answer was: {ans}")
        print(f"Your current score is {self.score}/{self.question_no} \n")

