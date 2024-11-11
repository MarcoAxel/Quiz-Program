class QuestionBank:
    """
    A class to manage a bank of questions and answers, supporting operations to load, write,
    add, and print question sets from a file.

    Attributes:
    -----------
    path : str
        The path to the file storing the question bank.
    dict : dict
        A dictionary containing questions as keys and answers (and decoys) as values.
    """

    def __init__(self, path=None, dict=None):
        """
        Initializes the QuestionBank with a file path and a dictionary for storing questions.

        Parameters:
        -----------
        path : str, optional
            The file path to load or save the question bank (default is None).
        dict : dict, optional
            A dictionary where questions are keys and values are lists of answers and decoys.
        """
        self.path = path
        self.dict = dict

    def load_bank_from_file(self):
        """
        Loads questions and answers from a file into a dictionary.
        
        The file should have questions and answers in the format:
        "Question:answer,decoy1,decoy2,decoy3"
        
        Returns:
        --------
        None
            Updates the object's dictionary attribute with questions and answers.
        """
        dict1 = {}
        with open(self.path, 'r') as file:
            question_list = file.readlines()
            for line in question_list:
                question_raw = line.split(':')
                q = question_raw[0]
                ans = question_raw[1]
                a = ans.split(',')
                a = [x.strip() for x in a if x.strip()]  # Remove any newline or extra spaces
                dict1[q] = a
        self.dict = dict1

    def write_bank_to_file(self):
        """
        Writes the current question bank dictionary to the file at the specified path.
        
        This method overwrites any existing content in the file with the current state of
        the dictionary, with each question-answer pair in the format:
        "Question:answer,decoy1,decoy2,decoy3"
        
        Returns:
        --------
        None
        """
        with open(self.path, 'w') as file:
            for question, answers in self.dict.items():
                answers_str = ",".join(answers)
                file.write(f'{question}:{answers_str}\n')

    def add_to_bank(self):
        """
        Adds new question and answer sets to the question bank dictionary.
        
        The user will be prompted to enter a question and four answer choices: one correct answer
        and three decoys. This method does not save changes to the file, but only updates the dictionary.

        Returns:
        --------
        None
        """
        num = int(input("Enter number of questions to add to the bank: "))
        for i in range(num):
            question = input("Enter question: ")
            answers = [input("Enter correct answer: ")]
            answers.extend(input("Enter decoy answer: ") for i in range(3))
            self.dict[question] = answers

    def print_bank(self):
        """
        Prints the questions and their corresponding answer lists from the dictionary.
        
        Format:
        -------
        Each question-answer pair is printed in the format:
        "Question: ['answer', 'decoy1', 'decoy2', 'decoy3']"

        Returns:
        --------
        None
        """
        for question, answers in self.dict.items():
            print(f'{question}: {answers}')
