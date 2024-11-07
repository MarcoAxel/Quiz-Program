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
    #So I added a class called system that basically handles logging in and logging out 
    #as well as accessing data I have not ran this yet, just a warning - Sencere
    class System:
        def __init__(self):
            # Mock user database with IDs and passwords 
            # (I think we can store all of the users in a 
            # csv or txt and then use that file to load the users dictionary)
            self.users = {
                'student1': Student(name="Bobby", userID="student1", password="password123", instructor="instructor1"),
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
                # will call methods that access specific data valuez
            elif isinstance(self.logged_in_user, Instructor): #checks if the current user is an instructor
                print("Accessing instructor data...")
                # will call methods that access specific data values
            else:
                print("No user is logged in.")

