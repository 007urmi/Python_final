from Question import Question


class System:
    def __init__(self):
        self.set_ques = []
        self.number_of_question = 0
        self.score = 0

    def addQuestion(self,topic,ques,ans):
        q = Question(topic,ques,ans)
        self.number_of_question +=1
        self.set_ques.append(q)
        return q
    def display(self):
        for question in self.set_ques:
            print(question.ques)
            print("\n\n")


    def runTest(self):
        for question in self.set_ques:
            print(question.topic)
            print(question.ques)
            answer = input("Enter your answer:")
            if answer.upper() == question.ans:
                self.score +=1
            else:
                print("The answer is:",question.ans)
        print("Total Score is:"+str(self.score)+" out of "+str(len(self.set_ques)))



