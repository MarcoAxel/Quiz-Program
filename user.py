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
        import csv
        #1)Looks for the specified "quiz_name.csv" file in the 'quizzes' directory, and loads it into a dictonary
        question_dict = {}
        total_questions = 0
        filepath = f"Quizfiles/{quiz_name}.csv"
        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # Each row in the CSV represents a question with answer options
                question = row[0]
                options = row[1:5]
                question_dict.update({question:options})
                total_questions +=1
        
        #2) if found it begins reading the question and prints them out one by one, along with the answer choices and waits for user answer choice input ('a','b','c', or 'd')
        import random as r
        running_score = 0
        for q,ans in question_dict.items():
            correct_ans = ans[0]
            r.shuffle(ans)
            print(q)
            for i in range(len(ans)):
                print(f"{i+1}) {ans[i]}")
            user_ans = int(input("Enter your answer as a number:"))
        #3) and then provides feedback, prints out current score and moves on to the next question until the quiz is over
            if ans[user_ans-1] == correct_ans:
                print("Correct!")
                running_score += 1
            else:
                print("Incorrect")
            print("-"*40)
            print(f"Current Score:{running_score}/{total_questions}")
            
        #4) provides test score and adds it to the scores dictionary
        final_score =(running_score/total_questions)*100
        print(f"Final Score:{final_score}")
        self.scores.update({quiz_name:final_score})
        

        
   
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
    #TODO add forgot password and security question(Maybe add attributes securityQuestion and securityQuestionAns )
class System:
    def __init__(self):
        # Mock user database with IDs and passwords 
        # (I think we can store all of the users in a 
        # csv or txt and then use that file to load the users dictionary)
        self.users = {
            'student1': Student(name="Bobby", userID="student1", password="p1", instructor="instructor1"),
            'instructor1': Instructor(name="Dr.Smith", userID="instructor1", password="totallySecurePassword")
        }
        self.logged_in_user = None

    def login(self, userID, password):
        """
        Logs in a user if credentials match those in the system.
        """
        user = self.users.get(userID)
        if user and user.password == password:
            self.logged_in_user = user
            print(f"Login successful. Welcome, {user.name}!")
            return True
        print("Login failed. Check your credentials.")
        return False

    def logout(self):
        """Logs out the current user."""
        self.logged_in_user = None
        print("Logged out successfully.")

    def access_user_data(self):
        """Provides access to the logged-in user's specific functionality."""
        if isinstance(self.logged_in_user, Student): #checks if the current user is a student
            print("Accessing student data...")
            # will call methods that access specific data values
        elif isinstance(self.logged_in_user, Instructor): #checks if the current user is an instructor
            print("Accessing instructor data...")
            # will call methods that access specific data values
        else:
            print("No user is logged in.")

