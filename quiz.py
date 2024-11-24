import os
import csv
import random

class Quiz:
    quiz_list={} #append all these new created quizzes into its respective => professor's quiz folder => in the quizes_list.txt file (this will allow us to update the quizzes list menu
    #creates a .csv file every time a quiz is created with its respective name, within  the <quizzes> folder in this python file's current file path
    #2 mandatory arguments:
        #quiz name:str= "New Quiz"
        #name of instructor creating the quiz":str=None
    
    #6 automatically set attributes
        #folder name 
        #empty questions list
        #question total sum set to 0
        #quizze's folder path [quiz folder name+ instructor name]
        #file name, replaces spaces to _ in quizz's name to make it its file name
        #combined filepath where quiz is to be created

    #It creates a new empty csv file for the questions of thuis quiz to be stored
    def __init__(self,quiz_name="New Quiz", instructor_name=None):
        self.quiz_name= quiz_name
        self.instructor_name= instructor_name
        self.folder_name="quizzes" 
        self.questions=[]
        self.size= 0 #total number of questions 

        #defined folder and file paths
        self.folder_path= os.path.join(self.folder_name,instructor_name)#self.folder_name +"/"+instructor_name
        self.quiz_file_name = f"{self.quiz_name.replace(' ','_').lower()}.csv"
        self.file_path = os.path.join(self.folder_path,self.quiz_file_name)

        #checking id folder exists
        os.makedirs(self.folder_path, exist_ok=True)

        #Create an empty .csv file for the quiz
        with open(self.file_path,mode="w",newline="")as quiz_csv_file:
            writer = csv.writer(quiz_csv_file)
            writer.writerow(["Question index","Question Text","Correct answer","Wrong answer 1","Wrong answer 2","Wrong answer 3"])
        
        print(f"New quiz {self.file_path} file path and csv file created!")

        #added new quiz to the quizzes list:
        self.quiz_list[self.quiz_file_name]= self.quiz_name

    def add_question(self,question_details=None):
        """creates a quiz-list[question#, question, correct_answer, wrong_ans*3] to be added to the list of quizes,
        then writes it ti the quiz csv file"""
        if question_details is None:
            question_details=[]
        self.size+=1
        print(f"Writing questions to quiz {self.quiz_name}: ")
        question_details.append(self.size)      #1st  item is the question #

        question= input(f"Type quiz question {self.size},  only the question:")
        question_details.append(question) #2nd item on the list is the question

        for i in range(4):
            if i <1:
                answer_choice= input(f"What is the correct answer {i+1}/4?")
                question_details.append(answer_choice) #3rd item is the correct answer choice
            else:
                answer_choice= input(f"What is the incorrect answer choice number {i+1}/4?")
                question_details.append(answer_choice) # 4-6 items in the list are wrong answer choices
        
        #Asks user to verify question and its answer choices, then writes question details in a row of the csv quiz file
        #TODO:

        with open(self.file_path,mode="a",newline="")as qf: #qf is an alias for quiz_cvs_file
            writer= csv.writer(qf)
            writer.writerow(question_details)

        #checks to see if the user wants to add more questions
        a=(input(f"Number of current questions in the quiz: {self.size}\nWould you like to add another question?[y/n]").lower().strip())
        again= None

        if a == "y" or a=="yes":
            again=True
        else:
            again=False

        if again:
            return self.add_question(question_details)
        else:
            print(f"Question writing to quiz completed. The total number of questions is {self.size}.")

    def delete_question(self, quiz_name="New Quiz", question_number=None):
        pass

    def display_questions(self,quiz_name="New Quiz"):
        print(f"Welcome to the online quiz system interface.\n {self.quiz_name} starting:")
        
        with open(self.file_path,mode="r")as qf:
            reader = csv.reader(qf)
            next(reader) #skips header files

            #breaks down the question details into its specific components
            for details in reader:
                q_index= details[0]
                q= details[1]
                a= details[2]
                f1= details[3]
                f2= details[4]
                f3= details[5]

                #creates a list of the answerchoices
                answer_choices=[a,f1,f2,f3]
                #creates a randomly shuffled version of answer choices list
                shuffled_answer_choices= random.sample(answer_choices,len(answer_choices))

                print(f"\nQuestion {q_index}:\n{q}")

                for choice in enumerate(shuffled_answer_choices,start=1):
                  print(f"{choice[0]}). {choice[1]}.")
                
                #asks user for an answer choice
                #checks if choice is valid
                while True:
                    try:
                        user_chosen_answer_index= -1+int(input(print("Enter your answer choice: \n (To select your choice, type a digit of 1-4, and the press 'Enter')")))
                        if 0<= user_chosen_answer_index <=4:
                            break
                        else:
                            print("Please enter a valid choice between 1 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 4.")

                #checks if correct
                correct=None
                if a == shuffled_answer_choices[user_chosen_answer_index]:
                    correct=True
                    print("correct")
                else:
                    correct=False
                    print("Wrong")
    @staticmethod              
    def menu():
        print("\n[0] End program" +
              "\n[1] to list quizzes" +
              "\n[2] create new quiz" +
              "\n[3] to choose and start a quiz")
        
    def main(self):
        Quiz.menu()
        user_input = int(input("Enter your option: "))
        
        
        while user_input != 0: #0 -> ends while loop and prints "Program terminated."
            if user_input == 1:
                # list quizes
                print("\nCopy and paste the name of the quiz you want to take")
                for i in self.quiz_list:
                    print(i)
            elif user_input == 2:
                # create a new quiz
                q_name=input("What is the quiz name:")
                i_name=input("What is the name of the instructor making the quiz: ")
                new_quiz= Quiz(q_name , i_name)
                new_quiz.add_question()
                pass
            elif user_input == 3:
                # choose and start a quiz
                pass
            else:
                #try new input
                print("Invalid input, try again:")
            Quiz.menu()
            user_input = int(input("Enter your option: "))

        print("Program terminated.")

