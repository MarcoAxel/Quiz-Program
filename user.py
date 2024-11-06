from quiz import Quiz     
class Student:
    def __init__(self,name= None, userID= None, password= None, instructor= None):
        self.name= name
        self.userID= userID
        self.password= password
        self.instructor= instructor
        self.average_grade= 0
        self.scores= {}
        self.quiz_counter= 0

    def increment_quiz_number(self):
        self.quiz_counter+=1
        return self.quiz_counter

    def clear_user_scores(self):
        self.quiz_counter= 0
        return 0
        
    def add_score(self,quiz_name ,score, date):
        """concats the name of the quiz taken and the quiz attempt number to associate the given score to it"""
        self.increment_quiz_number()
        instance= quiz_name + self.quiz_counter
        self.scores[instance]= [self.quiz_counter,score,date] #adds a key("quiz name + quiz counter"): value(a list [quiz number, quiz score, date quiz was taken]) pair to a dictionary which keeps track of quiz scores
        return self.scores

    def display_quiz_options(instructor_name):
        """"""
        pass

    def start_quiz(self,quiz_name):
        """ 1)Looks for the specified "quiz_name.csv" file in the 'quizzes' directory,
            2) if found it begins reading the question and prints them out one by one, along with the answer choices and waits for user answer choice input ('a','b','c', or 'd')
            3) and then provides feedback, prints out current score and moves on to the next question until the quiz is over
            4) provides test score and adds it to the scores dictionary
        """
        
        pass
   
class Instructor:
    def __init__(self,name= None, userID=None, password=None):
        self.name=name
        self.usedID= userID
        self.password=password
        self.students=[]
        self.quizzes=[]

    def create_quiz(self, quiz_name):
        new_quiz= Quiz(quiz_name , self.name)
        self.quizzes.append(new_quiz)
        print(f"Creating {quiz_name} quiz.")


        """import csv
        counter =1
        print("Creating a new {quiz_name} quiz")
        data = []
        cont= True
        while not cont: #loop ends when cont is set to false
            question_details= []
            user_input= input("Please type only the question type for quiz question {counter}.")
            counter+=1
            #finish
        with open("{quiz_name}.csv",mode ="w", newline="") as file:"""

    def delete_quiz():
        pass

    def display_grades():
        pass

    def display_quizzes():
        pass


    #notes, to identify we could use ID,and password if forgotten ask for name and a security question.
