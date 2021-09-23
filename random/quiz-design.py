

class Quiz:
    def __init__(self, id,category, desc):
        self.id = id
        self.questions = []
        self.category = category
        self.desc = desc
        self.timeLimit = 60

    def addQuestion(self, question):
        self.questions.add(question)

class Question:
    def __init__(self, question, answer, listOfOptions, maxScore):
        self.question = question
        self.answer = answer
        self.options = listOfOptions
        self.maxScore = maxScore

class BooleanQuestion(Question):
    def __init__(self, question, answer, listOfOptions, maxScore):
        self.super.__init__(question, answer, listOfOptions, maxScore)

class MCQQuestion(Question):
    def __init__(self, question, answer, listOfOptions, maxScore):
        self.super.__init__(question, answer, listOfOptions, maxScore)

class FillInTheBlankQuestion(Question):
    def __init__(self, question, answer, listOfOptions, maxScore):
        self.super.__init__(question, answer, listOfOptions, maxScore)


class Content:
    def __init__(self, content):
        self.content = content

class HtmlContent(Content):
    def __init__(self, content):
        self.super.__init__(self, content)

class TextContent(Content):
    def __init__(self, content):
        self.super.__init__(self, content)


class User:
    def __init__(self):
        pass




class AttemptQuiz:
    def __init__(self, quiz, user_id):
        self.user_id = user_id
        self.quiz = quiz
        self.score = None
        self.attemptedQuestion = []
        self.slowestQuestion = None

    def addAttemptedQuestion(self):
        pass

    def updateScore(self):
        pass



class AttemptQuestion:
    def __init__(self, question, user_id, duration, filledAnswer=None, ):
        self.user_id = user_id
        self.question = question
        self.score = None
        self.filledAnswer = filledAnswer
        self.answerLogs = []
        self.duration = duration

    def calculateScore(self):
        pass

    def fillAnswer(self):
        pass


class quizService:
    def __init__(self):
        quizRankMap = {} #{"quizID": [{"userID": userID, "score": "score", "rank": rank}]}



booleanQ = BooleanQuestion(TextContent(""), True, [True,False], 10)
mcQ = MCQQuestion(HtmlContent(""), [1,3], [HtmlContent(""), HtmlContent(""), HtmlContent(""), HtmlContent("")], 20)
blankQ = FillInTheBlankQuestion(HtmlContent(""), ["answer1","answer2"], [], 20)
q = Quiz("GK","GK Quiz")
q.addQuestion(booleanQ)
q.addQuestion(mcQ)
q.addQuestion(blankQ)









