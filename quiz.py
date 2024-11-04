import os
import csv

class Quiz:

    def __init__(self,quiz_name="New Quiz", instructor_name=None,folder_name="quizzes"):
        self.quiz_name= quiz_name
        self.instructor_name= instructor_name
        self.folder_name=folder_name 
        self.questions= []
        self.size= 0

        #defined folder and file paths
        self.folder_path= folder_name +"/"+instructor_name
        self.file_name = f"{self.quiz_name.replace(" ","_").lower()}.csv"
        self.file_path = os.path.join(self.folder_path,self.folder_name)

        #checking id folder exists
        os.makedirs(self.folder_path, exist_ok=True)

        #Create an empty .csv file for the quiz
        with open(self.file_path,mode="w",newline="")as quiz_csv_file:
            writer = csv.writer(quiz_csv_file)
        
        print(f"New quiz {self.file_path} file path and csv file created!")

    def add_question():
        pass

    def delete_question():
        pass

    def display_questions():
        pass

    def start_quiz():
        pass