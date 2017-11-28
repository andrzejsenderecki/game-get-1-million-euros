class QuestionEasy:

    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        self.quest = quest
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.answerGood = answerGood

    def printQuestion(self):
        print(self.quest)
        print(self.answerA)
        print(self.answerB)
        print(self.answerC)
        print(self.answerD)

class CheckAnswer:

    def checkAnswer(self):
        if answerPlayer == questionEasy1.answerGood:
            print('Good answer!')
        else:
            print('Bad answer!')

questionEasy1 = QuestionEasy('What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris','a')

checkAnswer = CheckAnswer()
questionEasy1.printQuestion()
print('You write good answer: a, b, c or d')
answerPlayer = input()
checkAnswer.checkAnswer()
