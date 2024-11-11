class question_bank:
    def __init__(self,path= None,dict = None):
        self.path = path
        self.dict = dict
    def load_bank_from_file(self):
        '''
        Loads questions from file into a dictonary and returns the dictonary 
        '''
        dict1 = {}
        file = open(self.path,'r')
        question_list = file.readlines()
        for i in question_list:
            question_raw = i.split(':')
            q = question_raw[0]
            ans = question_raw[1]
            a = ans.split(',')
            a.remove('\n')
            dict1.update({f'{q}':a})
        file.close()
        self.dict = dict1

    def write_bank_to_file(self):
        '''
        Takes the dictonary and writes it into the bank.txt file overwriting anything else in the file
        '''
        file = open(self.path, 'w')
        for key, val in self.dict.items():
            s = ""
            for i in val:
                s += i + ","
            file.write(f'{key}:{s}\n')

    def add_to_bank(self):
        '''
        Adds new items into the dictonary that stores the question bank DOES NOT write 
        the bank to a file
        ''' 
        dict1 = self.dict
        num = int(input("Enter number of questions to add to the bank:"))
        for i in range(num):
            q = input("Enter question:")
            a = []
            a.append(input("Enter answer:"))
            for j in range(3):
                a.append(input("Enter decoy answer:"))
            dict1.update({f'{q}':a})
            self.dict = dict1
        

    def print_bank(self):
        '''
        prints the key and values froma given dictonary 
        '''
        for key, val in self.dict.items():
            print(f'{key}:{val}')
            