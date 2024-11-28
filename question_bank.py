import csv
from tkinter import messagebox
class QuestionBank:
    """
    A class to manage a bank of questions and answers using CSV files, supporting operations to load, write,
    add, and print question sets.

    """

    def __init__(self, name=None, dict=None):
        """
        Initializes the QuestionBank with a file path and a dictionary for storing questions.

        Parameters:
        -----------
        path : str, optional
            The file path to load or save the question bank (default is None).
        dict : dict, optional
            A dictionary where questions are keys and values are lists of answers and decoys.
        """
        self.path = f"QuizFiles/{name}.csv"
        self.dict = dict if dict else {}

    def load_bank_from_csv(self):
        self.dict = {}
        try:
            with open(self.path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Skip empty rows
                        question = row[0]
                        answers = row[1:]
                        self.dict[question] = answers
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {self.path} not found.")

    def write_bank_to_csv(self):
        with open(self.path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for question, answers in self.dict.items():
                writer.writerow([question] + answers)

    def add_question(self, question, answers):
        self.dict[question] = answers
        self.write_bank_to_csv()

    def delete_question(self, question):
        if question in self.dict:
            del self.dict[question]
            self.write_bank_to_csv()
            return True
        return False
    
